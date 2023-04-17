# 입력처리 - input()함수
# 입력 방법 1
'''
print("이름을 입력해 주세요")
name = input() # 문자 입력 가능
'''

print()

# 입력 방법 2
'''
name = input("이름을 입력해 주세요 ")
print(name)
'''

# 입력받은 수는 문자열임 -> 정수로 변환 int() 함수 사용
'''
number = int(input("숫자를 입력해 주세요(1~10) "))
print(number * 2)
'''


# 두 수를 입력받아 합을 계산하기
'''
x = int(input("첫째 수 입력 : "))
y = int(input("둘째 수 입력 : "))
sum_v = x + y
print(sum_v)
'''

# 나이 계산
# 나이 = 현재년도 - 출생년도 + 1
# 태어난 년도를 입력해주세요
'''
current_year = 2023
birth_year = int(input("태어난 년도를 입력해 주세요. "))

age = current_year - birth_year + 1

print(str(age) + '세')
'''


# 넓이 계산 프로그램
# 넓이 = 가로 * 세로

width = int(input("가로의 길이 : "))
height = int(input("세로의 길이 : "))


area = width * height
print("가로 길이 : " + str(width) + "cm")
print("세로 길이 : " + str(height) + "cm")
print('면적 : ' + str(area) + 'cm')                










                 
