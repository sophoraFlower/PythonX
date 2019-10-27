import copy

"""
a = [1]
b = [1]
print(a == b)    # True
print(a is b)    # False

t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])
print(t1 == t2)    # True
print(t1 is t2)    # False

t1[-1].append(5)
print(t1 == t2)    # False
"""
"""
l1 = [[1, 2], (30, 40)]
# 深度拷贝
l2 = copy.deepcopy(l1)
l1.append(100)
l1[0].append(3)

print(l1)  # [[1, 2, 3], (30, 40), 100]
print(l2)  # [[1, 2], (30, 40)]

l3 = copy.copy(l1)
l3[1] += (50,)
print(l1)  # [[1, 2, 3], (30, 40), 100]
print(l3)  # [[1, 2, 3], (30, 40, 50), 100]
l3[0].append(4)
print(l1)  # [[1, 2, 3, 4], (30, 40), 100]
print(l2)  # [[1, 2], (30, 40)]
print(l3)  # [[1, 2, 3, 4], (30, 40, 50), 100]
"""

"""
x = [1]
x.append(x)
print(x)  # [1, [...]]
x = copy.copy(x)
print(x)

y = copy.deepcopy(x)
print(y)  # [1]
"""

"""
# 整形、字符串是不可变的
a = 1
print(id(a))
b = a
print(id(b))
# 重新创建了一个新的值为2的对象，并让a执行该对象
a = a + 1
print(id(a))
"""

"""
l1 = [1, 2, 3]
l2 = l1
print(id(l1))
print(id(l2))
# l1和l2同时指向这个列表，列表的变化会反映在l1和l2这两个变量上
l1.append(4)
print(id(l1))
print(id(l2))
print(l1 == l2)  # True
print(l1 is l2)  # True
"""

"""
# 参数为不可变值
def my_func1(b):
    print(id(b))
    b = 2
    print(id(b))


a = 1
print(id(a))
# 函数里，b is a
# b=2 使得 b指向对象2，b is not a
# 当执行到 b = 2 时，系统会重新创建一个值为 2 的新对象，并让 b 指向它；而 a 仍然指向 1 这个对象
my_func1(a)
# 函数外a仍不变
print(id(a))
print(a)  # 1
"""

"""
# 参数为可变值
def my_func(l2):
    print(id(l2))
    # l1 和 l2 先是同时指向值为 [1, 2, 3] 的列表。不过，由于列表可变，执行 append() 函数，对其末尾加入新元素 4 时，变量 l1 和 l2 的值也都随之改变
    l2.append(4)
    print(id(l2))


l1 = [1, 2, 3]
print(id(l1))
my_func(l1)
print(id(l1))
"""


def func(d):
    print("**" + str(d))
    print(id(d))
    d['a'] = 10
    print(id(d))
    print("***" + str(d))
    d['b'] = 20
    print(id(d))
    print("****" + str(d))


d = {'a': 1, 'b': 2}
print("*" + str(d))
print(id(d))
func(d)
print(id(d))
print("*****" + str(d))
