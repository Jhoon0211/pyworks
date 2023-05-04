"""
d = [
    [10, 20]
    [30, 40]
    [50, 60]
]


# 2차원 리스트 객체 출력
print(d)

# 전체 요소 (값) 출력
for x,y in d:
    print(x, y)


# 리스트 이름 = [요소1, 요소2, [값1, 값2]
e = [7, 3, ['chicken', 'eagle', 'monkey']]

print(e[1])  #3
print(e[2])
print(e[-1])

# eagle 출력
print(e[2][1])
print(e[-1][1])
"""

# 2차원 리스트 - 성적 통계
# 4명의 수학, 영어 과목의 총점과 평균
score = [
  # 수학, 영어
    [80, 70],
    [70, 80],
    [60, 90],
    [50, 75]
]


# 수학 [n][0] - 1열
# 영어 [0][n] - 2열

# 개인별 총점과 평균 - 저장 변수
total = 0

# 스코어의 길이
n = len(score)

print("개인별 총점 (수학 + 영어)")
for i in range(0, n):  # 0, 1, 2, 3
    total = score[i][0] + score[i][1]
    print(total)

print()
print("총점 평균")
# 개인별 평균 (수학 + 영어)
for i in range(0, n):  # 0, 1, 2, 3
    total = score[i][0] + score[i][1]
    print(total, total / 2)


# 과목별 총점과 평균
# sum_math=0, sum_eng=0
sum_subj = [0, 0]   # sum_subj[0] = 0(수학), sum_subj[1] = 0(영어)

# (0, n) = 4줄
for i in range(0, n):
    sum_subj[0] += score[i][0]  # 수학 합계
    sum_subj[1] += score[i][1]  # 영어 합계

# 과목별 총점
print()
print("과목별 총점과 평균")
print("수학총점 영어총점 수학평균 영어평균")
print(sum_subj[0]," "" "" "" ", sum_subj[1]," "" "" ",sum_subj[0]/len(score)," "" "" ",sum_subj[1]/len(score))
