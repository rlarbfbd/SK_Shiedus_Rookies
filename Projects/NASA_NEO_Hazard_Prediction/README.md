# NASA NEO Hazard Prediction

NASA Open API(NeoWs)를 활용하여 근지구 소행성(Near Earth Object, NEO) 데이터를 수집하고, 머신러닝을 이용해 소행성의 잠재적 위험 여부를 예측하는 프로젝트입니다.

본 프로젝트는 **SK 쉴더스 루키즈 교육과정을 통해 학습한 Python, 데이터 분석, 머신러닝, 딥러닝, Streamlit을 복습하고 실제 데이터에 적용하기 위해 진행하는 개인 프로젝트**입니다.

교육 과정에서 배운 내용을 단순히 실습으로 끝내는 것이 아니라, 공개 API를 활용한 데이터 수집부터 전처리, 모델 학습, 성능 평가, 웹 애플리케이션 구현까지 하나의 프로젝트로 직접 구현하며 학습 내용을 체계적으로 정리하고자 합니다.

---

## Project Purpose

이 프로젝트의 목적은 루키즈 교육과정에서 학습한 내용을 실제 프로젝트에 적용하며 복습하는 것입니다.

주요 목표는 다음과 같습니다.

- NASA Open API를 활용한 데이터 수집
- 데이터 전처리 및 탐색적 데이터 분석(EDA)
- 머신러닝 분류 모델 구현 및 성능 비교
- Streamlit을 활용한 웹 애플리케이션 개발
- Git/GitHub를 활용한 프로젝트 관리
- 프로젝트 진행 과정과 학습 내용을 체계적으로 기록

---

## Project Goals

- NASA NeoWs API를 이용한 실시간 데이터 수집
- 데이터 전처리 및 탐색적 데이터 분석(EDA)
- 머신러닝 분류 모델 구축
- 모델 성능 비교 및 평가
- 결과 시각화
- Streamlit 기반 대시보드 구현

---

## Tech Stack

### Language

- Python

### Libraries

- requests
- pandas
- numpy
- matplotlib
- scikit-learn
- streamlit
- jupyter
- python-dotenv

※ 프로젝트 진행에 따라 필요한 라이브러리를 추가할 예정입니다.

---

## Project Structure

```text
NASA_NEO_Hazard_Prediction/
│
├── data/
│   ├── raw/                  # 원본 데이터
│   └── processed/            # 전처리 데이터
│
├── notebooks/                # 실험 및 분석
│
├── src/                      # 프로젝트 소스 코드
│   ├── api.py
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── models/                   # 학습된 모델
│
├── results/                  # 결과 및 시각화
│
├── app/
│   └── streamlit_app.py      # Streamlit 애플리케이션
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Workflow

1. 프로젝트 구조 설계
2. NASA NeoWs API 연동
3. 데이터 수집
4. 데이터 전처리
5. 탐색적 데이터 분석(EDA)
6. 머신러닝 모델 학습
7. 모델 성능 비교
8. Streamlit 웹 애플리케이션 구현
9. 프로젝트 문서화

---

## Target

### 예측 대상

- `is_potentially_hazardous_asteroid`

### 입력 데이터(예정)

- 절대등급(H)
- 추정 최소 지름
- 추정 최대 지름
- 지구 접근 속도
- 최근접 거리
- 지구 접근 날짜

---

## Machine Learning Models

프로젝트 진행 과정에서 다양한 모델을 구현하고 성능을 비교합니다.

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest

최종적으로 가장 우수한 성능의 모델을 선정하여 Streamlit 애플리케이션에 적용할 예정입니다.

---

## Model Evaluation

다음 평가 지표를 활용하여 모델을 비교합니다.

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Streamlit Dashboard

최종적으로 Streamlit을 활용한 웹 애플리케이션을 구현합니다.

예정 기능

- NASA API 최신 데이터 조회
- 위험 소행성 여부 예측
- 예측 확률 표시
- 주요 데이터 시각화
- 모델 성능 비교
- 프로젝트 소개

---

## Project Status

- [x] 프로젝트 기획
- [ ] 프로젝트 구조 설계
- [ ] NASA API 연동
- [ ] 데이터 수집
- [ ] 데이터 전처리
- [ ] 탐색적 데이터 분석(EDA)
- [ ] 머신러닝 모델 구축
- [ ] 모델 성능 비교
- [ ] Streamlit 대시보드 구현
- [ ] 프로젝트 문서화

---

## Learning Objectives

이 프로젝트를 통해 다음 내용을 복습하고 실제 프로젝트에 적용합니다.

- Python
- REST API 활용
- JSON 데이터 처리
- 데이터 수집 자동화
- 데이터 전처리
- 탐색적 데이터 분석(EDA)
- 머신러닝 분류 모델
- 모델 성능 평가
- Streamlit 웹 애플리케이션 개발
- Git/GitHub를 활용한 프로젝트 관리

---

## Expected Results

- NASA API 기반 데이터 수집 시스템 구축
- 머신러닝 기반 위험 소행성 예측 모델 개발
- 모델 성능 비교 및 분석
- Streamlit 기반 웹 애플리케이션 구현
- 루키즈 교육과정에서 학습한 기술을 활용한 개인 프로젝트 완성

---

## Data Source

### NASA Open API

- NeoWs (Near Earth Object Web Service)

활용 데이터

- 근지구 소행성 정보
- 절대등급
- 추정 지름
- 지구 접근 거리
- 접근 속도
- 접근 날짜
- 잠재적 위험 여부

https://api.nasa.gov/

---

## License

This project is intended for educational purposes.

---

## Development Log

프로젝트 진행 과정과 학습 내용을 기록합니다.

| Date | Progress | Commit |
| :--- | :------- | :----- |
| 2026-08-13 | 프로젝트 기획 | 프로젝트 기획 |
| 2026-08-13 | 프로젝트 구조 설계 | 프로젝트 구조 생성 |
| - | NASA NeoWs API 연동 | - |
| - | 데이터 수집 모듈 구현 | - |
| - | 데이터 저장(CSV) 구현 | - |
| - | 데이터 전처리 | - |
| - | 탐색적 데이터 분석(EDA) | - |
| - | 머신러닝 모델 구현 | - |
| - | 모델 성능 비교 | - |
| - | Streamlit 대시보드 구현 | - |
| - | 프로젝트 문서화 | - |

---

## Future Improvements

프로젝트 완료 후 다음 기능을 추가하거나 개선할 예정입니다.

- SHAP을 활용한 모델 해석
- 하이퍼파라미터 튜닝
- 추가 머신러닝 모델 비교
- 최신 NASA 데이터 자동 갱신
- Streamlit UI 개선
- Docker를 활용한 프로젝트 실행 환경 구성

---

## References

- NASA Open API (NeoWs)
  - https://api.nasa.gov/
- Scikit-learn Documentation
  - https://scikit-learn.org/
- Streamlit Documentation
  - https://streamlit.io/