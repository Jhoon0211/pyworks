#접종 대상 : 20세 ~ 65세, 미 대상 - "하반기 일정 확인"

print("백신 접종자 분류")

# 출생년도 입력
birth_year = input("출생년도 입력 : ")

# 나이 계산
age = 2023 - int(birth_year) + 1
print(age)

#

if age >= 20 and age <= 65:
    print("백신 접종 대상")
    # 접종 대상 - 출생년도 끝자리 비교
    # if ~ elif ~ els
    birth_year = str(birth_year) # 문자열로 변환
    if birth_year[-1] == "1" or birth_year[-1] == "6":
        print("접종요일은 월요일입니다.")
    elif birth_year[-1] == "2" or birth_year[-1] == "7":
        print("접종요일은 화요일입니다.")
    elif birth_year[-1] == "3" or birth_year[-1] == "8":
        print("접종요일은 수요일입니다.")
    elif birth_year[-1] == "4" or birth_year[-1] == "9":
        print("접종요일은 목요일입니다.")
    else: 
        print("접종요일은 금요일입니다.")
        
else:
    print("하반기 일정 확인")
 
