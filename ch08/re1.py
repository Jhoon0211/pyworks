# re 모듈을 임포트함
import re
# 자바스크립트 - /정규표현식/g / 파이썬 - e.compile("정규표현식")
# 소문자 a부터 z까지 매치되는 문자를 반복해서 찾음
# match() - 일치하는 문자를 찾는 함수

# 정규표현식 삽입
p = re.compile("[a-z]+")

# match()는 처음 부터 일치 해야 검색 가능
m1 = p.match('afternoon')
print(m1)   # m1 객체
print(m1.group())   # 문자열 출력

m2 = p.match('2023 good luck')
print(m2)   # none - 숫자로 시작 해서 찾지 못함

# search()는 전체 중에 일치 하는 것이 하나라도 있으면 검색 가능
s1 = p.search('2023 good luck')
print(s1)
print(s1.group())