#!/usr/bin/env python3
from __future__ import annotations

"""Operational batch runner for Claude Code benchmark campaigns.

This driver keeps the existing per-run entrypoint (`run_claude_code`) and adds:
- fixed task/testcase/try ordering
- retry-priority resumption from the JSONL campaign log
- optional 4-way parallel execution with staggered launch
- per-run artifact verification and per-block validation
- early stop/report behavior for rate limits or other failures

It is intentionally operator-focused and expects dataset/log roots to be
configured by the operator for the current machine.
"""

import json
import os
import shutil
import subprocess
import sys
import time
import traceback
import zipfile
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from agent.claude_code.runner import run_claude_code  # noqa: E402


TASK_ORDER = [
    "zillow-prize-1",
    "ieee-fraud-detection",
    "sberbank-russian-housing-market",
    "home-credit-default-risk",
    "recruit-restaurant-visitor-forecasting",
]
TESTCASE_ORDER = [
    "tc1_from_scratch",
    "tc2_partial_good",
    "tc3_fault_injected",
    "tc4_mixed_history",
]
RUN_ORDER = ["try1", "try2", "try3", "try4", "try5"]
RATE_LIMIT_TERMS = [
    "rate limit",
    "429",
    "too many requests",
    "quota",
    "usage limit",
]
MAX_PARALLEL = 4
START_DELAY_SECONDS = 10
POLL_INTERVAL_SECONDS = 2

DOWNLOAD_ROOT_ENV = "KAGGLE_BENCH_DOWNLOAD_ROOT"
RECRUIT_ZIP_ROOT_ENV = "KAGGLE_BENCH_RECRUIT_ZIP_ROOT"
SBERBANK_COMPAT_ROOT_ENV = "KAGGLE_BENCH_SBERBANK_COMPAT_ROOT"
CAMPAIGN_LOG_PATH_ENV = "KAGGLE_BENCH_CLAUDE_CODE_CAMPAIGN_LOG"
DEFAULT_SBANK_COMPAT_ROOT = (REPO_ROOT / ".cache" / "sberbank-russian-housing-market").resolve()
DEFAULT_LOG_PATH = (REPO_ROOT / ".logs" / "claude_code_campaign.jsonl").resolve()


@dataclass(frozen=True)
class RunTarget:
    seq: int
    task_slug: str
    testcase_id: str
    run_id: str


def testcase_prefix(testcase_id: str) -> str:
    return testcase_id.split("_", 1)[0]


def task_dir_for(task_slug: str) -> Path:
    return REPO_ROOT / "data" / "tasks" / task_slug


def output_path_for(task_slug: str, testcase_id: str, run_id: str) -> Path:
    return task_dir_for(task_slug) / "outputs" / f"{testcase_prefix(testcase_id)}_claude_code_{run_id}.json"


def provenance_paths_for(task_slug: str, testcase_id: str, run_id: str) -> dict[str, Path]:
    prefix = testcase_prefix(testcase_id)
    base = task_dir_for(task_slug) / "outputs" / "provenance"
    stem = f"{prefix}_claude_code_{run_id}"
    return {
        "metadata_path": base / f"{stem}.meta.json",
        "trace_path": base / f"{stem}.trace.md",
        "prompt_path": base / f"{stem}.prompt.md",
        "stream_path": base / f"{stem}.stream.jsonl",
    }


def raw_prediction_path_for(task_slug: str, testcase_id: str, run_id: str) -> Path:
    prefix = testcase_prefix(testcase_id)
    base = task_dir_for(task_slug) / "outputs" / "provenance"
    return base / f"{prefix}_claude_code_{run_id}.raw_prediction.txt"


def build_targets() -> list[RunTarget]:
    targets: list[RunTarget] = []
    seq = 1
    for run_id in RUN_ORDER:
        for task_slug in TASK_ORDER:
            for testcase_id in TESTCASE_ORDER:
                targets.append(RunTarget(seq=seq, task_slug=task_slug, testcase_id=testcase_id, run_id=run_id))
                seq += 1
    return targets


def target_key(target: RunTarget) -> tuple[str, str, str]:
    return (target.task_slug, target.testcase_id, target.run_id)


def env_path(name: str) -> Path | None:
    raw = os.environ.get(name)
    if raw is None or not raw.strip():
        return None
    return Path(raw).expanduser().resolve()


def download_root() -> Path:
    configured = env_path(DOWNLOAD_ROOT_ENV)
    if configured is None:
        raise RuntimeError(
            f"{DOWNLOAD_ROOT_ENV} must point to the directory containing the benchmark task datasets."
        )
    return configured


def sberbank_source_root() -> Path:
    return (download_root() / "sberbank-russian-housing-market").resolve()


def sberbank_compat_root() -> Path:
    configured = env_path(SBERBANK_COMPAT_ROOT_ENV)
    if configured is not None:
        return configured
    return DEFAULT_SBANK_COMPAT_ROOT


def recruit_zip_root() -> Path:
    configured = env_path(RECRUIT_ZIP_ROOT_ENV)
    if configured is not None:
        return configured
    return (download_root() / "recruit-restaurant-visitor-forecasting" / "zip").resolve()


def campaign_log_path() -> Path:
    configured = env_path(CAMPAIGN_LOG_PATH_ENV)
    if configured is not None:
        return configured
    return DEFAULT_LOG_PATH


def append_log(payload: dict) -> None:
    log_path = campaign_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def print_step(message: str) -> None:
    print(message, flush=True)


def classify_failure(error_text: str) -> str:
    lowered = error_text.lower()
    for term in RATE_LIMIT_TERMS:
        if term in lowered:
            return "rate_limit"
    return "other"


def excerpt(text: str, limit: int = 600) -> str:
    compact = " ".join(text.split())
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3] + "..."


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def extract_single_member_zip(src: Path, dest: Path) -> None:
    with zipfile.ZipFile(src) as archive:
        member_names = [
            name
            for name in archive.namelist()
            if not name.endswith("/")
            and "/__MACOSX/" not in f"/{name}"
            and not Path(name).name.startswith("._")
        ]
        if len(member_names) != 1:
            raise RuntimeError(f"Expected exactly one CSV-like member inside {src}, found {len(member_names)}")
        with archive.open(member_names[0], "r") as read_handle, dest.open("wb") as write_handle:
            shutil.copyfileobj(read_handle, write_handle)


def prepare_sberbank_compat_root() -> Path:
    compat_root = sberbank_compat_root()
    compat_root.mkdir(parents=True, exist_ok=True)
    mapping = {
        "train.csv.zip": "train.csv",
        "test.csv.zip": "test.csv",
        "macro.csv.zip": "macro.csv",
        "sample_submission.csv.zip": "sample_submission.csv",
    }
    for zipped_name, plain_name in mapping.items():
        source = sberbank_source_root() / zipped_name
        destination = compat_root / plain_name
        if not source.exists():
            raise FileNotFoundError(f"Missing Sberbank source archive: {source}")
        extract_single_member_zip(source, destination)
    dictionary_source = sberbank_source_root() / "data_dictionary.txt"
    if not dictionary_source.exists():
        raise FileNotFoundError(f"Missing Sberbank data dictionary: {dictionary_source}")
    shutil.copyfile(dictionary_source, compat_root / "data_dictionary.txt")
    return compat_root


def resolve_data_root(task_slug: str) -> Path:
    if task_slug == "zillow-prize-1":
        return (download_root() / "zillow-prize-1").resolve()
    if task_slug == "ieee-fraud-detection":
        return (download_root() / "ieee-fraud-detection").resolve()
    if task_slug == "sberbank-russian-housing-market":
        return prepare_sberbank_compat_root()
    if task_slug == "home-credit-default-risk":
        return (download_root() / "home-credit-default-risk").resolve()
    if task_slug == "recruit-restaurant-visitor-forecasting":
        return recruit_zip_root()
    raise KeyError(f"Unsupported task slug: {task_slug}")


def verify_output(task_slug: str, testcase_id: str, run_id: str) -> None:
    testcase_path = task_dir_for(task_slug) / "testcases" / f"{testcase_id}.json"
    output_path = output_path_for(task_slug, testcase_id, run_id)
    result = run_command(
        [
            sys.executable,
            "eval/eval.py",
            "--testcase",
            str(testcase_path),
            "--input",
            str(output_path),
            "--stage-scope",
            "primary",
        ]
    )
    if result.returncode != 0:
        raise RuntimeError(
            "eval.py verification failed. "
            f"stdout={result.stdout!r} stderr={result.stderr!r}"
        )


def validate_artifacts() -> None:
    result = run_command([sys.executable, "eval/scripts/validate_artifacts.py"])
    if result.returncode != 0:
        raise RuntimeError(
            "validate_artifacts.py failed. "
            f"stdout={result.stdout!r} stderr={result.stderr!r}"
        )


def verify_artifact_bundle(task_slug: str, testcase_id: str, run_id: str) -> dict[str, str]:
    output_path = output_path_for(task_slug, testcase_id, run_id)
    provenance = provenance_paths_for(task_slug, testcase_id, run_id)
    expected_paths = {"output_path": output_path, **provenance}

    missing = [str(path) for path in expected_paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing expected artifact(s): {missing}")

    output_payload = json.loads(output_path.read_text(encoding="utf-8"))
    metadata_payload = json.loads(provenance["metadata_path"].read_text(encoding="utf-8"))

    if output_payload.get("testcase_id") != testcase_id or output_payload.get("run_id") != run_id:
        raise RuntimeError("Output payload metadata does not match expected testcase/run.")
    if metadata_payload.get("testcase_id") != testcase_id or metadata_payload.get("run_id") != run_id:
        raise RuntimeError("Metadata payload does not match expected testcase/run.")
    if metadata_payload.get("status") != "success":
        raise RuntimeError(f"Metadata status is not success: {metadata_payload.get('status')!r}")

    trace_size = provenance["trace_path"].stat().st_size
    prompt_size = provenance["prompt_path"].stat().st_size
    stream_size = provenance["stream_path"].stat().st_size
    if min(trace_size, prompt_size, stream_size) <= 0:
        raise RuntimeError("One or more provenance sidecars are empty.")

    verify_output(task_slug, testcase_id, run_id)
    return {name: str(path) for name, path in expected_paths.items()}


def cleanup_target_artifacts(target: RunTarget) -> None:
    paths = [
        output_path_for(target.task_slug, target.testcase_id, target.run_id),
        *provenance_paths_for(target.task_slug, target.testcase_id, target.run_id).values(),
        raw_prediction_path_for(target.task_slug, target.testcase_id, target.run_id),
    ]
    for path in paths:
        if path.exists():
            path.unlink()


def target_is_complete(target: RunTarget) -> bool:
    try:
        verify_artifact_bundle(target.task_slug, target.testcase_id, target.run_id)
        return True
    except Exception:
        return False


def load_failed_target_keys() -> list[tuple[str, str, str]]:
    log_path = campaign_log_path()
    if not log_path.exists():
        return []

    status_by_target: dict[tuple[str, str, str], str] = {}
    failure_order: list[tuple[str, str, str]] = []

    for raw_line in log_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue

        task_slug = payload.get("task_slug")
        testcase_id = payload.get("testcase_id")
        run_id = payload.get("run_id")
        if not all(isinstance(value, str) for value in (task_slug, testcase_id, run_id)):
            continue

        key = (task_slug, testcase_id, run_id)
        status = payload.get("status")
        if status == "failed":
            if key not in failure_order:
                failure_order.append(key)
            status_by_target[key] = "failed"
        elif status in {"success", "skipped_existing_success"}:
            status_by_target[key] = "success"

    return [key for key in failure_order if status_by_target.get(key) == "failed"]


def ensure_prerequisites() -> None:
    if shutil.which("claude") is None:
        raise RuntimeError("`claude` binary is not available on PATH.")
    for task_slug in TASK_ORDER:
        data_root = resolve_data_root(task_slug)
        if not data_root.exists():
            raise FileNotFoundError(f"Data root does not exist for {task_slug}: {data_root}")


def worker_summary(
    success: bool,
    *,
    target: RunTarget,
    created_paths: dict[str, str] | None,
    failure_type: str | None,
    error_text: str | None,
) -> dict:
    return {
        "success": success,
        "seq": target.seq,
        "task_slug": target.task_slug,
        "testcase_id": target.testcase_id,
        "run_id": target.run_id,
        "failure_type": failure_type,
        "error_excerpt": excerpt(error_text or "") if error_text else None,
        "created_paths": created_paths,
        "output_path": str(output_path_for(target.task_slug, target.testcase_id, target.run_id)),
        "log_path": str(campaign_log_path()),
    }


def run_single_target(target: RunTarget) -> int:
    try:
        created_paths = verify_artifact_bundle(target.task_slug, target.testcase_id, target.run_id)
        append_log(
            {
                "seq": target.seq,
                "task_slug": target.task_slug,
                "testcase_id": target.testcase_id,
                "run_id": target.run_id,
                "status": "skipped_existing_success",
                "output_path": created_paths["output_path"],
                "error_excerpt": None,
            }
        )
        print(json.dumps(worker_summary(True, target=target, created_paths=created_paths, failure_type=None, error_text=None)))
        return 0
    except Exception:
        pass

    cleanup_target_artifacts(target)
    append_log(
        {
            "seq": target.seq,
            "task_slug": target.task_slug,
            "testcase_id": target.testcase_id,
            "run_id": target.run_id,
            "status": "started",
            "output_path": str(output_path_for(target.task_slug, target.testcase_id, target.run_id)),
            "error_excerpt": None,
        }
    )

    try:
        run_claude_code(
            task_dir=task_dir_for(target.task_slug),
            testcase_id=target.testcase_id,
            run_id=target.run_id,
            data_root=resolve_data_root(target.task_slug),
        )
        created_paths = verify_artifact_bundle(target.task_slug, target.testcase_id, target.run_id)
        append_log(
            {
                "seq": target.seq,
                "task_slug": target.task_slug,
                "testcase_id": target.testcase_id,
                "run_id": target.run_id,
                "status": "success",
                "output_path": created_paths["output_path"],
                "error_excerpt": None,
            }
        )
        print(json.dumps(worker_summary(True, target=target, created_paths=created_paths, failure_type=None, error_text=None)))
        return 0
    except Exception as exc:
        error_text = f"{exc}\n{traceback.format_exc()}"
        failure_type = classify_failure(error_text)
        append_log(
            {
                "seq": target.seq,
                "task_slug": target.task_slug,
                "testcase_id": target.testcase_id,
                "run_id": target.run_id,
                "status": "failed",
                "failure_type": failure_type,
                "output_path": str(output_path_for(target.task_slug, target.testcase_id, target.run_id)),
                "error_excerpt": excerpt(error_text),
            }
        )
        print(json.dumps(worker_summary(False, target=target, created_paths=None, failure_type=failure_type, error_text=error_text)))
        return 2 if failure_type == "rate_limit" else 1


def parse_worker_summary(stdout: str) -> dict:
    lines = [line for line in stdout.splitlines() if line.strip()]
    if not lines:
        raise RuntimeError("Worker produced no stdout summary.")
    return json.loads(lines[-1])


def maybe_validate_completed_block(done_targets: set[tuple[str, str, str]], target: RunTarget) -> bool:
    needed = {(target.task_slug, testcase_id, target.run_id) for testcase_id in TESTCASE_ORDER}
    if not needed.issubset(done_targets):
        return False
    validate_artifacts()
    return True


def resume_targets() -> tuple[list[RunTarget], set[tuple[str, str, str]]]:
    pending: list[RunTarget] = []
    done_targets: set[tuple[str, str, str]] = set()
    failed_target_keys = load_failed_target_keys()
    for target in build_targets():
        if target_is_complete(target):
            done_targets.add(target_key(target))
            continue
        cleanup_target_artifacts(target)
        pending.append(target)

    failure_rank = {key: index for index, key in enumerate(failed_target_keys)}
    pending.sort(
        key=lambda target: (
            0 if target_key(target) in failure_rank else 1,
            failure_rank.get(target_key(target), target.seq),
            target.seq,
        )
    )
    return pending, done_targets


def launch_worker(target: RunTarget) -> subprocess.Popen[str]:
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--worker",
        target.task_slug,
        target.testcase_id,
        target.run_id,
        str(target.seq),
    ]
    return subprocess.Popen(
        command,
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def run_parallel_campaign() -> int:
    ensure_prerequisites()
    log_path = campaign_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    append_log({"status": "session_start", "max_parallel": MAX_PARALLEL, "start_delay_seconds": START_DELAY_SECONDS})

    pending_targets, done_targets = resume_targets()
    failed_target_keys = set(load_failed_target_keys())
    print_step(f"Existing successful runs kept: {len(done_targets)}")
    print_step(f"Remaining runs to execute: {len(pending_targets)}")
    if failed_target_keys:
        print_step(
            "Retry priority targets: "
            + ", ".join(
                f"{task_slug}:{testcase_id}:{run_id}"
                for task_slug, testcase_id, run_id in sorted(failed_target_keys)
            )
        )

    last_success: dict | None = None
    completed_count = len(done_targets)

    for offset in range(0, len(pending_targets), MAX_PARALLEL):
        batch = pending_targets[offset: offset + MAX_PARALLEL]
        print_step(
            "Launching batch: "
            + ", ".join(f"{target.seq}:{target.task_slug}:{target.testcase_id}:{target.run_id}" for target in batch)
        )

        active: list[tuple[RunTarget, subprocess.Popen[str]]] = []
        stop_launching_batch = False
        failure_summary: dict | None = None
        failure_exit_code: int | None = None

        def collect_finished_processes() -> list[tuple[RunTarget, subprocess.Popen[str], dict]]:
            finished: list[tuple[RunTarget, subprocess.Popen[str], dict]] = []
            for target, process in list(active):
                if process.poll() is None:
                    continue
                stdout, stderr = process.communicate()
                try:
                    summary = parse_worker_summary(stdout)
                except Exception as exc:
                    error_text = f"Could not parse worker summary: {exc}. stdout={stdout!r} stderr={stderr!r}"
                    summary = worker_summary(
                        False,
                        target=target,
                        created_paths=None,
                        failure_type=classify_failure(error_text),
                        error_text=error_text,
                    )
                finished.append((target, process, summary))
                active.remove((target, process))
            return finished

        def handle_finished_processes(
            finished: list[tuple[RunTarget, subprocess.Popen[str], dict]],
        ) -> None:
            nonlocal completed_count, last_success, stop_launching_batch, failure_summary, failure_exit_code

            for target, _process, summary in finished:
                if summary["success"]:
                    completed_count += 1
                    done_targets.add((target.task_slug, target.testcase_id, target.run_id))
                    last_success = {
                        "seq": target.seq,
                        "task_slug": target.task_slug,
                        "testcase_id": target.testcase_id,
                        "run_id": target.run_id,
                        "output_path": summary["output_path"],
                    }
                    files_checked = summary["created_paths"] or {}
                    print_step(
                        f"[success] {target.seq}/100 {target.task_slug} {target.testcase_id} {target.run_id} "
                        f"files_ok={sorted(files_checked)}"
                    )
                    if maybe_validate_completed_block(done_targets, target):
                        print_step(f"[validated] block {target.run_id} / {target.task_slug}")
                    continue

                if failure_summary is None:
                    stop_launching_batch = True
                    failure_summary = {
                        "completed_count": None,
                        "last_success": None,
                        "failed_target": {
                            "seq": target.seq,
                            "task_slug": target.task_slug,
                            "testcase_id": target.testcase_id,
                            "run_id": target.run_id,
                        },
                        "failure_type": summary["failure_type"],
                        "error_excerpt": summary["error_excerpt"],
                        "created_outputs": [],
                        "log_path": str(log_path),
                    }
                    failure_exit_code = 2 if summary["failure_type"] == "rate_limit" else 1
                    print_step(
                        f"[failure] {target.seq}/100 {target.task_slug} {target.testcase_id} {target.run_id} "
                        f"type={summary['failure_type']} active_peers_will_drain={len(active)}"
                    )

        for index, target in enumerate(batch):
            process = launch_worker(target)
            active.append((target, process))
            print_step(f"[launch] {target.seq}/100 {target.task_slug} {target.testcase_id} {target.run_id}")
            if index < len(batch) - 1:
                deadline = time.time() + START_DELAY_SECONDS
                while time.time() < deadline:
                    finished = collect_finished_processes()
                    if finished:
                        handle_finished_processes(finished)
                    if stop_launching_batch:
                        break
                    time.sleep(min(POLL_INTERVAL_SECONDS, max(0.0, deadline - time.time())))
            if stop_launching_batch:
                print_step("[batch] failure detected during stagger delay; pausing further launches")
                break

        while active:
            time.sleep(POLL_INTERVAL_SECONDS)
            finished = collect_finished_processes()
            if finished:
                handle_finished_processes(finished)

        if failure_summary is not None:
            failure_summary["completed_count"] = completed_count
            failure_summary["last_success"] = last_success
            failure_summary["created_outputs"] = sorted(
                str(output_path_for(task_slug, testcase_id, run_id))
                for task_slug, testcase_id, run_id in done_targets
            )
            print(json.dumps(failure_summary, indent=2), flush=True)
            return failure_exit_code or 1

    append_log({"status": "session_complete", "completed_count": completed_count})
    summary = {
        "completed_count": completed_count,
        "last_success": last_success,
        "failure_type": None,
        "error_excerpt": None,
        "created_outputs": sorted(
            str(output_path_for(task_slug, testcase_id, run_id))
            for task_slug, testcase_id, run_id in done_targets
        ),
        "log_path": str(log_path),
    }
    print(json.dumps(summary, indent=2), flush=True)
    return 0


def parse_worker_args(argv: list[str]) -> RunTarget:
    if len(argv) != 5 or argv[0] != "--worker":
        raise SystemExit(
            "Usage: run_claude_code_campaign.py --worker <task_slug> <testcase_id> <run_id> <seq>"
        )
    return RunTarget(seq=int(argv[4]), task_slug=argv[1], testcase_id=argv[2], run_id=argv[3])


def main(argv: list[str]) -> int:
    if argv[:1] == ["--worker"]:
        target = parse_worker_args(argv)
        return run_single_target(target)
    return run_parallel_campaign()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
