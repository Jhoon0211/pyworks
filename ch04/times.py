# 배수를 구하는 함수를 정의하고 사용
#

"""
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=' ')
"""

def times(x):
    global count  # 전역 변수
    for i in range(1,101):
        if i % x == 0:
            count += 1
            print(i, end=' ')
    print()
    print(count)
count = 0
times(3)
print(f'\n배수의 개수 : {count}')