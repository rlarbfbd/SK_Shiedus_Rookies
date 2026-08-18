# NASA NeoWs API 컬럼 정리

## 최상위 컬럼

| 컬럼명 | 설명 | 머신러닝 사용 여부 |
| :--- | :--- | :---: |
| `links` | 해당 소행성 API 정보 링크 | ❌ |
| `id` | NASA에서 부여한 소행성 고유 ID | ❌ |
| `neo_reference_id` | NEO 데이터베이스 참조 ID | ❌ |
| `name` | 소행성 이름 | ❌ |
| `nasa_jpl_url` | NASA JPL 상세 정보 페이지 URL | ❌ |
| `absolute_magnitude_h` | 소행성의 절대등급(H). 값이 작을수록 밝고 일반적으로 크기가 큰 소행성 | ✅ |
| `estimated_diameter` | 소행성의 추정 지름(단위별 제공) | ✅ |
| `is_potentially_hazardous_asteroid` | 잠재적 위험 소행성 여부(True/False) | ⭐ Target |
| `close_approach_data` | 지구 접근 정보(날짜, 속도, 거리 등) | ✅ |
| `is_sentry_object` | NASA Sentry 위험 감시 시스템 등록 여부 | △ |

---

## estimated_diameter

소행성의 추정 크기를 다양한 단위로 제공.

### kilometers

| 컬럼명 | 설명 | 사용 여부 |
| :--- | :--- | :---: |
| `estimated_diameter_min` | 추정 최소 지름(km) | ✅ |
| `estimated_diameter_max` | 추정 최대 지름(km) | ✅ |

### meters

| 컬럼명 | 설명 | 사용 여부 |
| :--- | :--- | :---: |
| `estimated_diameter_min` | 추정 최소 지름(m) | ❌ |
| `estimated_diameter_max` | 추정 최대 지름(m) | ❌ |

### miles

| 컬럼명 | 설명 | 사용 여부 |
| :--- | :--- | :---: |
| `estimated_diameter_min` | 추정 최소 지름(mi) | ❌ |
| `estimated_diameter_max` | 추정 최대 지름(mi) | ❌ |

### feet

| 컬럼명 | 설명 | 사용 여부 |
| :--- | :--- | :---: |
| `estimated_diameter_min` | 추정 최소 지름(ft) | ❌ |
| `estimated_diameter_max` | 추정 최대 지름(ft) | ❌ |

> 프로젝트에서는 **kilometers 단위만 사용**.

---

## close_approach_data

소행성이 지구에 접근하는 정보를 담고 있음.

| 컬럼명 | 설명 | 사용 여부 |
| :--- | :--- | :---: |
| `close_approach_date` | 지구 접근 날짜 | ✅ |
| `close_approach_date_full` | 지구 접근 날짜 및 시간 | △ |
| `epoch_date_close_approach` | 접근 시각(Epoch Timestamp) | ❌ |
| `relative_velocity` | 접근 속도 정보 | ✅ |
| `miss_distance` | 지구와의 최근접 거리 | ✅ |
| `orbiting_body` | 기준 천체(대부분 Earth) | ❌ |

---

## relative_velocity

소행성의 접근 속도를 다양한 단위로 제공.

| 컬럼명 | 설명 | 사용 여부 |
| :--- | :--- | :---: |
| `kilometers_per_second` | 초당 속도(km/s) | ❌ |
| `kilometers_per_hour` | 시간당 속도(km/h) | ✅ |
| `miles_per_hour` | 시간당 속도(mi/h) | ❌ |

> 프로젝트에서는 **kilometers_per_hour**를 사용.

---

## miss_distance

지구와의 최근접 거리를 다양한 단위로 제공.

| 컬럼명 | 설명 | 사용 여부 |
| :--- | :--- | :---: |
| `astronomical` | 천문단위(AU) | ❌ |
| `lunar` | 달과의 거리 기준 | ❌ |
| `kilometers` | 최근접 거리(km) | ✅ |
| `miles` | 최근접 거리(mi) | ❌ |

> 프로젝트에서는 **kilometers**를 사용.

---

# 머신러닝 학습에 사용할 Feature

| Feature | 설명 |
| :--- | :--- |
| `absolute_magnitude_h` | 절대등급(H) |
| `estimated_diameter_min` | 추정 최소 지름(km) |
| `estimated_diameter_max` | 추정 최대 지름(km) |
| `relative_velocity_kilometers_per_hour` | 지구 접근 속도(km/h) |
| `miss_distance_kilometers` | 지구와의 최근접 거리(km) |

---

# Target

| Target | 설명 |
| :--- | :--- |
| `is_potentially_hazardous_asteroid` | 잠재적 위험 소행성 여부(True / False) |