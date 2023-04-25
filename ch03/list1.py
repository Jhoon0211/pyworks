# 리스트 생성
# 빈 리스트
cart = []

# 리스트 추가방식 1. appned()
cart.append('계란')
cart.append('사과')
cart.append('생수')
cart.append('콩나물')

# 특정한 위치에 요소 추가
cart.insert(2, "양파")

# 리스트 개수
print(len(cart))

# 리스트 삭제방식 1.
#del cart[0]

# 리스트 수정
cart[2] = '커피'

# 리스트 추가방식 2. cart = []
# cart2 = ['엽떡', '과자', '훈제란']

# 리스트 삭제방식 2. (특정요소 삭제)
# cart2.remove('과자')

# 맨 뒤에 삭제
cart.pop()

# 전체 조회 = 전체 요소의 수 0, 1, 2 증가하며 표출
for i in cart:
    print(i)

# 리스트 출력
print(cart)

# 특정한 값 조회
# print(cart[2])
#print(cart2)
