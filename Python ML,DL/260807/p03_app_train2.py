# 딥러닝 학습 -> 파일 저장

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import numpy as np

# 데이터 생성
np.random.seed(42)

X = np.random.rand(100, 10)
y = np.random.randint(0, 2, 100)
y = to_categorical(y)

# 모델 정의
model = Sequential([
    Dense(32, activation="relu", input_shape=(10, )),

    Dense(2, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X, y,
    epochs=5,
    batch_size=10,
    verbose=1
)

# 모델 저장
model.save("keras_model.keras")
print("save ok")

