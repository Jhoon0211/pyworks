# 이분 탐색
"""
자료가 크기 순서대로 정렬된 리스트에서 특정한 값이 있는지
찾아 그 위치를 돌려주는 알고리즘

☆ 탐색 과정
1. 중간 위치를 찾는다.
2. 찾는 값과 중간 위치값을 비교한다.
3. 찾는 값이 중간 위치 값보다 크면 중간 위치의 오른쪽을 대상으로
    탐색하고, 작으면 왼쪽을 대상으로 탐색한다.
"""

def bin_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if x == a[mid]:
            return mid  # 위치값 찾음
        elif x > a[mid]:    # 찾는 값이 중간값보다 크면
            start = mid + 1 # 오른쪽 범위를 좁혀 계속 탐색
        else:               # 찾는 값이 중간값보다 작으면
            end = mid - 1   # 왼쪽 범위를 좁혀 계속 탐색

    return -1 # 찾는 값이 없으면

#d = [1,4,9,16,25,36,49,64,81]
d = [49, 4, 64, 25, 36, 81, 16, 9, 1]

# 정렬 - 오름차순
d.sort()
print(d)

print(bin_search(d, 49)) # 6
print(bin_search(d, 50)) # -1

"""
찾는 값이 36일 경우
1. mid = (0+8)//2=4, a[4]=25 중간 위치값
2. 49>25 25의 오른쪽 범위
3. mid = (5+8)//2=6, a[6]=49 찾음
4. 36<49 49의 왼쪽 범위 탐색
5. 36 - 1개 찾음.
"""