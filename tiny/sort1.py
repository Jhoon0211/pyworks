# 정렬 - 1. 내장함수 2. 반복조건문
# 리스트의 메서드 sort(), reverse()

a = [1, 5, 4, 15, 6]
"""
a.reverse()   # 거꾸로 배치 - [6, 15, 4, 5, 1]
print(a)

a.sort()
print(a)    # 오름차순 - [1, 4, 5, 6, 15]

a.sort(reverse=True)
print(a)    # 내림차순 - [15, 6, 5, 4, 1]
"""

a = [60, 5, 33, 12, 97, 24]
# 2. 반복 조건문(중첩 for)
# 정렬 알고리즘 - 버블정렬
n = len(a)
for i in range(0, n):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            # 교환 자리바꾸기
            a[j], a[j+1] = a[j+1], a[j]

# 디버깅
'''
i=0(1행) a[0] > a[1] False 1, 5
         a[1] > a[2] True 1, 4, 5
         a[2] > a[3] False 1, 4, 5, 15
         a[3] > a[4] False 1, 4, 5, 6, 15

'''

print(a)






