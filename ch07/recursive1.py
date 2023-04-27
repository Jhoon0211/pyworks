# 재귀 함수
# 종료 조건을 항상 명시(if ~ else)
# 재귀함수로 "Help me!" 표출
def sos(n):
    print("Help me!")
    # 종료 조건
    if n == 1:
        return ""
    else:
        return sos(n-1)

    """
    n=3, help me!, sos(2)
    n=2, help me! help me!, sos(1)
    n=1, help me! help me! help me!
    """

#sos(5)

# 1부터 5까지 곱하기
gob = 1  # 곱셈은 0으로 초기화 하는 것이 아닌 1로 기억
for i in range(1, 6):
    gob *= i
    print(i, gob)

# 1부터 5까지 곱하기 (함수 사용)
def getgob(n):
    gob = 1  # 곱셈은 0으로 초기화 하는 것이 아닌 1로 기억
    for i in range(1, 6):
        gob *= i
        #print(i, gob)
    return gob

# 1부터 5까지 곱하기 (재귀함수 사용)
# 5*4(5-1)*3(4-1)*2(3-1)*1(2-1) = 5!(팩토리얼, 계승)
# 패턴을 코드화
"""
def func(입력 값):
    if 입력 값이 충분히 작으면: # 종료 조건
        return 결과 값
    else: # 입력 값 보다 더 작은 값으로 호출
        return 결과 값
"""
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

    """
    n=5, 5 * facto(4)
    n=4, 5 * 4 * facto(3)
    n=3, 5 * 4 * 3 * facto(2)
    n=2, 5 * 4 * 3 * 2 * facto(1)
    """

# getgob() 호출
print(getgob(5))