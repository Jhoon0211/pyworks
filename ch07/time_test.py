import time
"""

start = time.time()
def getgob(n):
    gob = 1  # 곱셈은 0으로 초기화 하는 것이 아닌 1로 기억
    for i in range(1, n+1):
        gob += i
        #print(i, gob)
    return gob

print(getgob(100000))
end = time.time()
print(f'소요시간 : {end-start}')
"""
start = time.time()

def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(998))
end = time.time()
print(f'소요시간 : {end-start:.6f}')
