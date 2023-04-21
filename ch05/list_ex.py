# 리스트 복사
a = [1, 2, 3, 4]
a2 = []

# 3의 배수 표출
'''
for i in a:
    a2.append(3 * i)
print(a2)
'''

# 3의 배수 내포문 표출
# 리스트 내포 - for문이 리스트 내부
a3 = [3 * i for i in a]
print(a3)

# 3의 배수이면서 짝수인 수를 구하시오
a4 = []
for i in a:
    if i % 2 == 0:
        a4.append(3 * i)
print(a4)

# 리스트 내포 -  3의 배수이면서 짝수인 수
a4 = [3 * i for i in a if i % 2 == 0]
print(a4)

# 1부터 10까지 저장하는 리스트
b = [i for i in range(1, 11)]
print(b)

# 1에서 10까지의 자연수를 저장
c = {x for x in range(1,14)}
print(c)

# 1에서 20까지의 자연수 중에서 3의 배수 저장
d = {x for x in range(1, 21) if x % 3 == 0}
print(d)