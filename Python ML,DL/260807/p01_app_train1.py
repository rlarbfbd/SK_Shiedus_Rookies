# 머신러닝 학습 후 파일 저장

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# 파일 저장용 lib
import joblib       # 확장자 : .joblib(최근에는 .joblib 사용 권장) or .pkl

X,y = make_regression(
    n_samples=100,
    n_features=1,
    noise=0.1,
    random_state=42
)

model = LinearRegression()

model.fit(X, y)

# 모델 => 파일로 저장
joblib.dump(model, "model.joblib")

print("save ok")

