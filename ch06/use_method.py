import method1 as met
from method1 import get_sum2, get_num

# import method1 as met인 경우
# get_sum2() 호출
val = met.get_sum2(10)
print(val)

# from method1 import get_sum2
val2 = get_sum2(10)
print(val2)

# get_num() 호출 - 자동방식
met.get_num(10)