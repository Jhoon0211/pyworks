# 시간 - time 모듈
import time

# 1970. 1. 1 자정이후 지금까지 시간을 초로 환산
print(time.time())

# round() - 반올림 (정수로 반올림)
year = round(time.time()/(365*24*60*60))
day = round(time.time()/(24*60*60))
print(f"{year}년")
print(day)

# 연도, 월, 일, 시, 분, 초
print(time.localtime())

# 날짜와 시간 형태로 표기
print(time.ctime())

# 시간 측정
# 종료 시간(time.time()) - 시작 시간(time.time())
# time.sleep(1)- 1초대기
# 1부터 10000가지 출력 하는 데 걸리는 시간
start = time.time()

for i in range(1, 101):
    print(i)

end = time.time()
print(f'{end-start:.3f}')