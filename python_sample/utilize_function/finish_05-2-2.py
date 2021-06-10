minNum = 2
maxNum = 10
totalNum = 100
memo = {}

def problem(remain, used):
    key = str([remain, used])
    # 종료 조건
    if key in memo:
        return memo[key]
    if remain < 0:
        return 0       # 무효이므로 0을 리턴
    if remain == 0:
        return 1       # 유효하므로 수를 세기 위해 1을 리턴

    # 재귀 처리
    output = 0
    for i in range(used, maxNum + 1):
        output += problem(remain - i, i)

    # 메모화 처리
    memo[key] = output

    # 종료
    return output

print(problem(totalNum, minNum))