# 모델을 로드해서 추론하는 모듈

from sklearn.datasets import make_regression

# 저장된 모델 파일 로드 모듈
import joblib

X, y = make_regression(
    n_samples=10,
    n_features=1,
    noise=0.1
)

# 모델 파일 로드
print("모델 로드 시작")

loaded_model = joblib.load("model.joblib")

print("모델 로드 종료")

# 모델을 이용한 추론
y_pred = loaded_model.predict(X)
print(y_pred)

