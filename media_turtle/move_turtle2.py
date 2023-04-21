# turtle 모듈
import turtle as t

t.shape("turtle")
t.bgcolor("greenyellow")

n = 4 # 변의 개수
d = 100 # 거리 (크기)

for i in range(4):
    t.forward(100)
    t.left(90)

t.mainloop()