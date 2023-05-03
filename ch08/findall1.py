import re


str="123?45yy7890 hi 999 hello"

#pat = re.compile('\d{1,3}')   # 0~9사이의 숫자가 1개~3개 배열을 찾음
#m = re.findall(pat, str)

# 위에 두 식을 한개로 축약 가능
m = re.findall('\d{1,3}', str)
print(m)

m2 = re.findall('[1-5]{1,2}', str)
print(m2)


"""
# '*', '+'의 차이
# * = 앞의 문자가 0번 이상 반복 될 경우 표출(없어도 찾음)
p = re.compile('ca*t')
m1 = re.findall(p, 'caat')
print(m1)

m2 = re.findall(p, 'ct')
print(m2)

# + = 앞의 문자가 1번 이상 반복 될 경우 표출
p2 = re.compile('ca+t')
m3 = re.findall(p2, 'caat')
print(m3)

# + = 앞의 문자가 1번 이상 반복 될 경우 표출(없으면 못찾음)
m4 = re.findall(p2, 'ct')
print(m4)
"""

# 점(.)은 임의의 문자 - 소괄호는 서브클래스(그룹)
str = "abcd<hr>Thank you"
pat1 = re.compile("<(.*)>") # 태그 미포함
m1 = re.findall(pat1, str)
print(m1)

pat2 = re.compile("(<.*>)") # 태그 포함
m2 =  re.findall(pat2, str)
print(m2)