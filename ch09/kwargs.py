# 키워드 매개변수
# 딕셔너리 형의 자료로 만들어짐

def print_kw(**kwargs):
    print(kwargs)

# 호출
print_kw(name='진')
print_kw(age=30, gender='여자')

# 가변 매개변수 - *
def calc_sum(*numbers):
    sum_v = 0
    for i in numbers:
        sum_v += i
    return sum_v

print(calc_sum(1, 53))
print(calc_sum(1, 53, 547))

9 + 4

125060
119080