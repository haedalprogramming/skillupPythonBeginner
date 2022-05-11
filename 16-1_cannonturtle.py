"""거북이 대포 게임 만들기
1. turn_up/turn_down 함수
    사용자가 위와 아래 방향키를 누르면 대포 각도를 조절합니다
2. fire 함수
    사용자가 SpaceBar를 누르면 작동
    거북이 대포를 발사하고 
    대포가 땅에 닿으면 목표 지점을 맞혔는지 문자 출력
3. 게임 준비 및 실행 부분
    땅, 목표지점, 대포 위치를 지정하고 화면에 그리기
    사용자가 키보드를 누르면 올바른 함수가 실행되도록 예약
"""

import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)
    
    d = t.distance(target, 0)
    t.sety(random.randint(10, 100))
    if d < 25:
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)

t.goto(-300, 0)
t.down()
t.goto(300, 0)

target = random.randint(50, 150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen()
t.done()