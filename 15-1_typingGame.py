"""타자 게임 만들기
1. 사전 준비
    게임에 필요한 모듈을 임포트
    사용자가 게임을 시작할 준비를 하고
    Enter를 누를 때까지 기다리기
2. 메인 프로그램
    사용자에게 문제를 보여주고 타자 입력을 받고
    처리하는 과정을 5번 반복
    (오타가 나면 5번을 넘을 수 있어 while 사용)
3. 결과를 계산해서 보여주기
    사용자가 타자 문제를 모두 입력하는데 걸린 시간을
    소수점 둘째자리까지 계산해 출력
"""
import random
import time

# 
word = ["cat", "dog", "fox", "monkey", 
        "mouse", "panda", "frog", 
        "snake", "wolf"]
# 
num = 1
print("[타자 게임] 준비되면 엔터")
# 
input()

# 
start = time.time()

# 
ques = random.choice(word)
# 
while num <= 5:
    print("*문제", num)
    # 
    print(ques)
    # 
    answer = input()
    # 
    if ques == answer:
        # 통과 출력
        print("통과!")
        # 
        num = num + 1
        # 
        ques = random.choice(word)
    else:
        print("오타! 다시 도전")

# 
end = time.time()
# 
interval = end - start
# 
interval = format(interval, ".2f")
# 
print("타자 시간 :", interval, "초")

# 응용하기
# 1. word 리스트에 다른 동물이름 추가하기
# 2. 한글 문장을 리스트에 추가하기