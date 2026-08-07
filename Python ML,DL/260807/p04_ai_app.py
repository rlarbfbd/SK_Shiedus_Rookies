# 저장된 모델 로드 -> 추론

from tensorflow.keras.models import load_model
import numpy as np

# 모델 로드
loaded_model = load_model("keras_model.keras")

print("loaded ok")

# 추론
sample_data = np.random.rand(1, 10)
predictions = loaded_model.predict(sample_data)

print(predictions)

