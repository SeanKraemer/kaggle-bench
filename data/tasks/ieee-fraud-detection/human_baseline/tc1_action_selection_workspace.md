# TC1 Human Output Selection Workspace

이 문서는 `tc1_from_scratch` human output의 최종 selection 기록이다.

검토 방식:
- IEEE candidate bank 전체를 군별로 나눠 순서대로 검토했다.
- 각 군에서 직접 고른 action id만 기록한다.
- 자동 보정이나 dependency completion은 하지 않았다.

## 1. Join

- 선택: `CA-000005`
- 보류 메모: 없음

## 2. Expression-based Feature Engineering

- 선택: 없음
- 보류 메모: 군 전체 검토 후 미선택

## 3. Time Handling

- 선택: `CA-000003`, `CA-000025`, `CA-000089`
- 보류 메모: dependency 자동 보정 없음

## 4. Category / String Handling

- 선택: `CA-000069`
- 보류 메모: 없음

## 5. Categorical Encoding

- 선택: `CA-000034`
- 보류 메모: 없음

## 6. Aggregation / Sequence Features

- 선택: `CA-000043`
- 보류 메모: 없음

## 7. Numeric Transforms

- 선택: `CA-000066`, `CA-000054`, `CA-000083`
- 보류 메모: 없음

## 8. Interaction Features

- 선택: 없음
- 보류 메모: 군 전체 검토 후 미선택

## 9. Missingness Handling

- 선택: `CA-000032`, `CA-000033`, `CA-000047`
- 보류 메모: 없음

## 10. Binning / Type Coercion

- 선택: 없음
- 보류 메모: 군 전체 검토 후 미선택

## 11. Pruning / Filtering / Reduction

- 선택: `CA-000027`, `CA-000028`, `CA-000029`
- 보류 메모: dependency 자동 보정 없음

## 12. Outlier Handling

- 선택: `CA-000011`
- 보류 메모: 없음

## Final Assembly Notes

- 최종 선택 action ids: `CA-000005`, `CA-000003`, `CA-000025`, `CA-000089`, `CA-000069`, `CA-000034`, `CA-000043`, `CA-000066`, `CA-000054`, `CA-000083`, `CA-000032`, `CA-000033`, `CA-000047`, `CA-000027`, `CA-000028`, `CA-000029`, `CA-000011`
- 최종 미선택 군: `Expression-based Feature Engineering`, `Interaction Features`, `Binning / Type Coercion`
- 의존성 확인 메모: `CA-000025 -> CA-000020` 미선택
- 의존성 확인 메모: `CA-000029 -> CA-000010` 미선택
- 남은 확인 사항: 필요하면 evaluator 기준 coherence review 별도 수행
