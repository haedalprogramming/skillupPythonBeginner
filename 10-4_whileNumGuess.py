# while 무한 반복 
# while True:
	# print("영원히~")

# -> break로 반복을 멈춘다

import random

# 
n = random.randint(1, 30)

# 
while True:
	x = input("숫자를 맞춰보자: ")
	# 
	g = int(x)
	# 
	if g == n:
		print("정답")
		# 
		break
	if g < n:
		print("너무 작아요")
	if g > n:
		print("너무 커요")