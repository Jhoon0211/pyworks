# 딕셔너리
# d = {'키': 값}
d = {'Tomas':13, 'Jane':9}

# 요소 추가 - Mike가 10살.
d['Mike'] = 10
print(d)

# 모든 키 가져오기
print(d.keys())

# 모든 값(value) 가져오기
print(d.values())
print(list(d.values()))

# 모든 키와 값 가져오기 - values()
for key, val in d.items():
    print(key, ':', val)



