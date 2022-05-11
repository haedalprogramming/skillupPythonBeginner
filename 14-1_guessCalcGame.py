"""계산 맞히기 게임 만들기
1. 사용자에게 제시할 계산 문제를 만드는 make_question 함수
	계산에 필요한 숫자를 2개 만든 후 연산자를 고르고 계산 문제를 완성
2. 메인 프로그램
	계산 맞히기 게임을 진행하고, 정답/오답 횟수를 사용자에게 보여줌
"""
import random

def make_question():
    """make_question 
    목적: 사용자에게 제시할 계산문제를 만듭니다
    구성: 숫자1 연산자 숫자2 
    예시: 1+3 2*10 11-7 
    """
    # 
    a = random.randint(1,40)
    # 
    b = random.randint(1,20)
    # 
    op = random.randint(1,3)

    # 
    # 변수 이름으로 question의 q를 따옴 
    # 
    q = str(a)

    # 연산자 추가
    # 
    if op == 1:
        q = q + "+"
    # 
    if op == 2:
        q = q + "-"
    # 
    if op == 3:
        q = q + "*"
    
    # 
    q = q + str(b)

    # 
    return q



# 
correct = 0
wrong = 0

# 다섯 문제를 풀어보자
for x in range(5):
    # 
    q = make_question()
    # 
    print(q)
    # 
    ans = input("=")
    # 
    r = int(ans)
    
    # 컴퓨터가 계산한 결과를 사용자가 입력한 결과와 비교
    if eval(q) == r:
        print("정답!")
        correct = correct + 1
    else:
        print("오답!")
        wrong = wrong + 1
# 
print("정답: ", correct, "오답: ", wrong)
# 
if wrong == 0:
    print("당신은 똑똑이 땅땅땅")

# 응용하기
# 문제를 조금 더 다양하게 만들어볼까요?
# 1. random.randint 수치 범위를 수정해 더 큰 숫자가 나오게 하기
# 2. 소숫점이 필요한 나눗셈 문제 추가