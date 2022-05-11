def sum_func(n):
    """sum_func(n)
1부터 n까지의 합을 결과값으로 돌려주는 함수
여기는 docstring입니다
    """
    # 
    s = 0
    # 
    for x in range(1, n+1):
        # 
        s = s + x
        # 
    return s

# 
print(sum_func(10))
print(sum_func(100))
print(sum_func.__doc__)
# help(sum_func)