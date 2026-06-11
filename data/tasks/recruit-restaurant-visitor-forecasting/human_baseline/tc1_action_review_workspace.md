# Recruit TC1 Human Action Review Workspace

이 문서는 `tc1_from_scratch` human output 작성을 위한 작업대다.
여기서는 bank의 `good` 액션들을 검토하기 쉽게 카테고리만 나눈다.
선택 판단이나 추천은 적지 않는다.

## 1. Reservation Time Prep

- reservation datetime parsing
- reservation lead-time / time-gap feature

## 2. Reservation Aggregate Features

- reservation aggregate at `(air_store_id, visit_date)` grain
- reservation aggregate join-back to prediction rows

## 3. Visit-Date Features

- visit-date parsing
- date-part extraction from `visit_date`

## 4. Historical Demand Features

- grouped historical visitor summaries by store / weekday

## 5. Core Lookup Joins

- holiday / calendar lookup join
- air store metadata join

## 6. Core Encoding And Target Transform

- categorical encoding for store metadata
- target log transform

## 7. HPG Bridge And Reservation Synthesis

- `store_id_relation` bridge from `hpg_store_id` to `air_store_id`
- cross-source reservation synthesis features

## 8. Weighted-Mean Holiday Branch

- holiday normalization for weekend handling
- weighted mean demand lookup using holiday-aware grouping

## 9. String Normalization

- normalization for `air_genre_name`
- normalization for `air_area_name`

## 10. Fill Policy Branch

- model-specific missing-value fill policy
