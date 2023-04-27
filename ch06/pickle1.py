# pickle 모듈 사용
# 객체(리스트, 딕셔너리) 형태를 그대로 유지하여 저항하고 읽어옴
# pickle.dump - 쓰기, pickle.load - 읽기

import pickle

# 쓰기
with open("./output/object.txt", "wb") as f:
    a = ['강아지', '고양이', '말']
    dic = {1: '강아지', 2: '고양이', 3: '말'}
    pickle.dump(a, f)
    pickle.dump(dic, f)

# 읽기
with open("./output/object.txt", "rb") as f:
    a = pickle.load(f)
    dic = pickle.load(f)

    print(a)
    print(dic)
