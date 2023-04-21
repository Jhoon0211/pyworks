# turtle 모듈
import turtle as t

# 사각형 그리며 이동
'''
t.shape("turtle")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
'''

# 삼각형을 그리며 이동
t.color('blue')
'''
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
'''

for i in range(4):
    t.forward(100)
    t.left(90)

t.color('blue')
for i in range(3):
    t.forward(100)
    t.left(120)

t.color('red')
t.pensize(3)
t.circle(50)

t.mainloop()