import turtle as t

# 
angle = 89
# 
t.bgcolor("black")
# 
t.color("yellow")
# 
t.speed(0)
# 
for x in range(200):
	# 
	t.forward(x)
	# 
	t.left(angle)
t.done()

# 응용하기
# 1. angle = 89에서 왼쪽으로 회전할 각도를 바꾸면 신기한 모양이 그려집니다.
# angle 값을 45, 90, 100 등으로 다양하며 바꾸며 거북이가 그린 그림을 실습합니다