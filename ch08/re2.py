import re

# findall(정규식, 문자열) - 문자열 검색 / match()와 유사하나 결과를 리스트로 반환

str = "Two is too"
m1 = re.findall("T[wo]o", str)  #[wo] - 'w' or 'o'와 일치
print(m1)   # ['Two']

# IGNORECASE 대소문자 허용
m2 = re.findall("T[wo]o", str, re.IGNORECASE)
print(m2)

m3 = re.findall("T[^o]o", str, re.IGNORECASE)   # [^W] - 'w'가 아닌 문자
print(m3)