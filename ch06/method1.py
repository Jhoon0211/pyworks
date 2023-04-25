import time
"""
for i in range(1, 11):
    print(i)
"""

# 1부터 n까지 출력 하는 함수
def get_num(n):
    for i in range(1, n+1):
        print(i, end=' ')

# 호출
get_num(20)

# 1부터 n까지 합계를 구하는 함수
start = time.time()
def get_sum(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v +=i
    return sum_v

print(f'합계 : {get_sum(10000)}')
end = time.time()
print(f'소요 시간 : {end-start}초')




# 1부터 n까지 합계를 구하는 함수 - time 함수 사용시 조금 더 빠름
# 계산 복잡도 - 곱셉, 덧셈, 나눗셈 - 3번 : 0(1)
start = time.time()
def get_sum2(n):
    sum_v = (n * (n+1)) // 2
    return sum_v

if __name__=="__main__":
    print(f'합계2 : {get_sum2(1000000000)}')
    end = time.time()
    print(f'소요 시간 : {end-start}초')


