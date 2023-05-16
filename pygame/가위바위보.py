"""
가위, 바위, 보 게임 만들기

 - 게임 방법
1. 당신(you)은 가위, 바위, 보 중 하나를 입력한다.
2. 컴퓨터(com)는 가위, 바위, 보 중 하나를 랜덤 생성한다.
3. 결과 출력은 무승부, 패, 승이다.
4. 잘못 입력한 경우 "잘못된 입력입니다. 다시 입력해주세요"
"""

import random
import sys

print("♠ 가위 바위 보 게임 ♠")
가위바위보 = ['가위', '바위', '보']

you = input('당신 : ')

com = random.choice(가위바위보)
print("컴퓨터 :", com)

"""
rnd = random.randint(0, 2)
com = 가위바위보[rnd]
print("컴퓨터 :", com)
"""

if you not in 가위바위보:    # x in y 문
    print("잘못된 입력입니다. 다시 입력해주세요")
    sys.exit(0)  # 프로그램 즉시 종료


    # 사용자가 이길 경우만 코드를 할당하고 무승부와 패에는 if, else로 처리
if you == com:
    print('결과 : 무승부')
elif you == '가위' and com == '보':
        print("결과 : 승")
elif you == '바위' and com == '가위':
        print("결과 : 승")
elif you == '보' and com == '가위':
        print("결과 : 승")
else:
    print("결과 : 패")


