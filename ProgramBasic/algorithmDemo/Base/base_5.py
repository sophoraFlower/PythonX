def factorial(n):
    """ 计算n的阶乘，n必须是正整数 """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


t = 0.0000000001
N = 20
print(t * factorial(N))
