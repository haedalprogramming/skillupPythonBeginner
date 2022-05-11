import time

# 
input("엔터를 누르고 20초를 셉니다")
# 
start = time.time()

# 
input("20초 후에 다시 엔터를 누릅니다.")
# 
end = time.time()

#  
# 
interval = end - start
# 출력하자
print("실제 시간: ", interval, "초")
print("차이 :", abs(interval-20), "초")