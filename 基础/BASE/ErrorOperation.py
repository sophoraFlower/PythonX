# coding:utf8

try:
    num = eval(input("请输入一个整数："))
    print(num**2)
except NameError:
    print("输入不是整数")
else:
    print("AAA")
finally:
    print("输入不确定")
