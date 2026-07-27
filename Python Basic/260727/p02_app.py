# app.py도 모듈 -> 외부에 있는 모듈 사용

# import mod1         # 파일의 이름이 모듈의 이름
# import mod1 as m
# from mod1 import PI, add, sub
# from mod1 import *
# import mod.mod2 as m
# from mod.mod2 import PI, add, sub
from mod.mod2 import *

print("__name__", __name__)             # __main__

print("app.py 실행 시작")

# 3번 라인
# print(mod1.PI)
# print(mod1.add(23585675619, 2937857))
# print(mod1.sub(23585675619, 2937857))

# 4,7번 라인
# print(m.PI)
# print(m.add(23585675619, 2937857))
# print(m.sub(23585675619, 2937857))

# 5,6,8,9번 라인
print(PI)
print(add(1, 2))
print(sub(1, 2))

print("app.py 실행 종료")