import random

# 
a = random.randint(1,30)
# 
b = random.randint(1,30)

# 문제를 출력
print(a, "+", b, "=")
# 
x = input()
# 
c = int(x)

if a + b == c:
	print("천재!")
else:
	print("바보?")

# 응용하기
# if c == a+b : 라고 작성해도 동일하게 작동합니다