# 피보나치 수열 - 1 1 2 3 5 8 13 21 . . .
# 첫째항 및 둘째 항이 1이며, 그 뒤의 항은 바로 앞 두항의 합

def fibo(n):
    if n <= 2:   # 종료 조건
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

    """
    n=1, fibo(1),  1
    n=2, fibo(2),  1
    n=3, fibo(3), fibo(1) + fibo(2),   2
    n=4, fibo(4), fibo(2) + fibo(3),   3
    n=5, fibo(5), fibo(3) + fibo(4),   5
    n=6, fibo(6), fibo(4) + fibo(5),   8
    n=7, fibo(7), fibo(5) + fibo(6),   13
    
    """


print(fibo(1))     # 1
print(fibo(2))     # 1
print(fibo(3))     # 2
print(fibo(4))     # 3
print(fibo(5))     # 5
print(fibo(6))     # 8
print(fibo(7))     # 13
print(fibo(8))     # 21
print(fibo(9))     # 34
