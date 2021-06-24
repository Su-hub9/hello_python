# 모듈을 가져옵니다.
from functools import wraps
import functools

# 함수로 데코레이터를 생성합니다.
def test(function):
    @wraps(function)
    def wrapper(*arg, **kwargs):
        print("인사가 시작되었습니다.")
        function(*arg, **kwargs)
        print("인사가 종료되었습니다.")
    return wrapper

# 데코레이터를 붙여 함수를 만듭니다.
@test
def hello():
    print("hello")

# 함수를 호출합니다.
hello()