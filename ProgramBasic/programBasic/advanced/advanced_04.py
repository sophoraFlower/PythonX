def my_func(b):
    b = 2


def my_fun2(b):
    b = 2
    return b


def my_func3(lx):
    # 影响原变量
    lx.append(4)


def my_func4(lx):
    # 不影响原变量
    lx = lx + [4]


def my_func5(lx):
    # 推荐写法
    lx = l2 + [4]
    return lx


a1 = 1
a2 = 1
my_func(a1)
my_fun2(a2)
a3 = my_fun2(a2)
print(a1)
print(a2)
print(a3)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
my_func3(l1)
print(l1)  # [1, 2, 3, 4]
my_func4(l2)
print(l2)  # [1, 2, 3]
l3 = my_func5(l1)
print(l3)  # [1, 2, 3, 4]

