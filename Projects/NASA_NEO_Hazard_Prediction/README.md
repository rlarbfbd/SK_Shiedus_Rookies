# NASA NEO Hazard Prediction

NASA Open API(NeoWs)를 활용하여 근지구 소행성(Near Earth Object, NEO) 데이터를 수집하고, 머신러닝을 이용해 소행성의 잠재적 위험 여부를 예측하는 프로젝트입니다.

본 프로젝트는 **SK 쉴더스 루키즈 머신러닝·딥러닝 교육과정에서 학습한 Python, 데이터 분석, 머신러닝, Streamlit을 실제 데이터에 적용**하는 것을 목표로 진행합니다.

---

## Project Goals

- NASA NeoWs API를 이용한 실시간 데이터 수집
- 데이터 전처리 및 탐색적 데이터 분석(EDA)
- 머신러닝 분류 모델 구축 및 성능 비교
- 모델 해석 및 결과 시각화
- Streamlit을 활용한 웹 대시보드 구현

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
├── models/                   # 학습된 모델 저장
│
├── results/                  # 결과 및 시각화
│
├── app/
│   └── streamlit_app.py      # Streamlit 웹 애플리케이션
│
├── README.md
└── requirements.txt
```

---

## Workflow

1. NASA NeoWs API 분석
2. 데이터 수집
3. 데이터 전처리
4. 탐색적 데이터 분석(EDA)
5. 특징 선택 및 데이터 준비
6. 머신러닝 모델 학습
7. 모델 성능 평가 및 비교
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

다양한 머신러닝 모델을 학습하고 성능을 비교하여 최적의 모델을 선정합니다.

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest

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

최종적으로 Streamlit을 이용하여 웹 기반 대시보드를 구현합니다.

### 주요 기능

- NASA API 최신 데이터 조회
- 위험 소행성 여부 예측
- 예측 확률 표시
- 소행성 정보 시각화
- 머신러닝 모델 성능 비교
- 프로젝트 소개 및 데이터 출처 제공

---

## Project Status

- [x] 프로젝트 기획
- [x] 프로젝트 구조 설계
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

본 프로젝트를 통해 다음 내용을 학습하고 적용합니다.

- REST API 활용
- JSON 데이터 처리
- 데이터 수집 자동화
- 데이터 전처리
- 탐색적 데이터 분석(EDA)
- 데이터 시각화
- 머신러닝 분류 모델
- 모델 성능 평가
- Streamlit 웹 애플리케이션 개발
- Git/GitHub를 활용한 프로젝트 관리

---

## Expected Results

- NASA API 기반 데이터 수집 시스템 구축
- 머신러닝 기반 위험 소행성 예측 모델 개발
- 모델 성능 비교 및 분석
- Streamlit을 활용한 대시보드 구현
- 루키즈 교육과정에서 학습한 내용을 종합적으로 활용한 프로젝트 완성

---

## Data Source

- NASA Open API (NeoWs)
- https://api.nasa.gov/

---

## License

This project is intended for educational purposes.