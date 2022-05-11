import turtle as t
# 
import random

# 거북이 모양의 그래픽을 사용
t.shape("turtle")
# 거북이 속도 최대
t.speed(0)

# 거북이를 500번 움직이자
for x in range(500):
	# 1~360 중 아무 수를 골라 direction에 저장
	direction = random.randint(1,360)
	# 거북이 방향을 direction 각도로 돌립니다
	t.setheading(direction)
	# 
	distance = random.randint(1,20)
	# 
	t.forward(distance)

# 응용하기
# 1. direction = random.randint(1,180)으로 수정해보기
# -> 화면 밖으로 나갈거임
# 2. distance = random.randint(1,40)으로 수정하기
# -> 거북이가 움직이는 거리가 늘어남