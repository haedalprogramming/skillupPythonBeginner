import turtle as t

# 
n = 5
t.color("purple")
# 
t.begin_fill()
# 
for x in range(n):
	# 
	t.forward(50)
	# 
	t.left(360/n)
# 
t.end_fill()
t.done()

# 응용하기
# 1. n값을 3,4,6,8,10 등으로 고쳐 다양한 정다각형을 그려봅니다.
# 2. n값이 클수록 점점 원에 가까워지는데 너무 큰 값을 입력하면 다각형이 화면 밖으로 나갑니다
# 3. forward(50)의 길이를 줄여 화면에 맞게 적당히 줄여봅니다