print("__name__", __name__)

print('mod.mod2.py 실행 시작')

PI = 3.14

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

print('mod.mod2.py 실행 종료')

if __name__ == "__main__":
    # 모듈의 기능들을 테스트
    print(PI)
    print(add(10, 5))
    print(sub(10, 5))