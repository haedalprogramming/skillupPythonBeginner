import turtle as t

# 
n = 50
# 
t.bgcolor("black")
# 
t.color("green")
# 
t.speed(0)
# 
for x in range(n):
	# 
	t.circle(80)
	# 
	t.left(360/n)

# 응용하기
# 1. 배경색과 펜 색을 바꿔보기
# 2. n값을 50이 아닌 다른 수로 입력
# 3. t.circle(80) -> t.circle(x*2)