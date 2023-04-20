# 함수 - 입력기능 (매개변수를 통해서)
# 사각형의 넓이 계산 함수 (넓이 = 가로의 길이 X 세로의 길이)
# 삼각형의 넓이 계산 함수 (넓이 = 밑변 X 높이) / 2

# 사각형
# 함수 이름 - calc_area()
def calc_area(w, h):
    area = w * h
    return area    

# 가로 - 4cm, 세로 - 3cm
print('사각형의 면적 :', calc_area(4, 3))

# f 스트링 방식
result = calc_area(4, 3)
print('사각형의 면적 :', result)
print(f'사각형의 면적 : {result}')


# 삼각형
# 함수 이름 - tri_area()

# 밑변 - 4cm, 높이 - 5
def tri_area(s, h):
    area = (s * h) / 2
    return area

print('삼각형의 면적 :', tri_area(4, 5))

result = tri_area(4,5)
print('삼각형의 면적 :', result)
print(f'삼각형의 면적 : {result}')


# 정사각형의 면적
'''
size = int(input("숫자를 입력: "))
area = size * size
print(area)
'''
def calc_size(n):
    area = n * n
    return(area)

print(calc_size(100))





