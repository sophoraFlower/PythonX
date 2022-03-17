import sys

a = []

# 两次引用，一次来自 a，一次来自 getrefcount
print(sys.getrefcount(a))  # 2


def func(a_):
    # 四次引用，a，python的函数调用栈，函数参数，和 getrefcount
    print(sys.getrefcount(a_))  # 4


func(a)

# 两次引用，一次来自 a，一次来自 getrefcount，函数 func 调用已经不存在
print(sys.getrefcount(a))  # 2
