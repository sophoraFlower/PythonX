def factorial(n):
    """ 计算n的阶乘，n必须是正整数 """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


N = eval(input("请输入正整数："))
print(N, "的阶乘结果是 = ", factorial(N))
