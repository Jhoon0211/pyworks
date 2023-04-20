# 리스트
a = [1, 2, 3, 4]
print(a)

# 리스트에 5 추가
a.append(5)
print(a)

# 5를 삭제
a.pop()

print(a)

a2 = [] # a2라는 빈 리스트 생성
'''
a2 = a # 직접 복사
print(a2)


# for ~ in로 복사
for i in a:
    a2.append(i)
print(a2)
'''

# a 리스트의 합계와 평균
sum_v = 0
for i in a:
    sum_v += i
print(f'[a] 합계 : {sum_v}')


avg_v = sum_v / len(a) # 평균
print(f'[a] 평균 : {avg_v}')

# 내장함수
print(sum(a)) # 리스트를 더한 것

b = [1, 2, 3, 4] # 튜플을 더한 것
print(sum(b))

# 3의 배수로 복사
for i in a:
    a2.append(3*i)
print(a2)


# a리스트에서 홀수만 저장
a3 = []
for i in a:
    if i % 2 != 0:
    #if i % 2 == 1:
        a3.append(i)
print(a3)
