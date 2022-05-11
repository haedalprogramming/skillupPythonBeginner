def factorial(n):
	"""factorial(n)
1부터 n까지의 곱을 결과값으로 돌려주는 함수
여기는 docstring입니다
	"""
	# 
	fact = 1
	# 
	for x in range(1, n+1):
		# 
		fact = fact * x
	# 
	return fact

print(factorial(5))
print(factorial(10))

# 팩토리얼이 뭐에요?
# 1부터 n까지의 양의 정수를 모두 곱한 것을 수학에서는 팩토리얼이라 부릅니다
# 느낌표를 사용해 n!로 표시합니다.
# 2 팩토리얼 : 2! = 1*2 = 2
# 5 팩토리얼 : 5! = 1*2*3*4*5 = 120 
# 10팩토리얼 : 10! = 1*2*3*4*5*6*7*8*9*10 = 3628800
# 단, 0!은 1이라고 약속합니다