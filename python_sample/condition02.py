# 입력을 받습니다.
number = input("정수 입력> ")
last_charactor = number[-1]

# 짝수 조건
if last_charactor in "02468":
    print("짝수입니다")

# 홀수 조건
if last_charactor in "13579":
    print("홀수입니다")