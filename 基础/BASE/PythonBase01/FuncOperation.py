# coding:utf8

"""
func = lambda x, y: x + y
print(func(10, 15))
"""


def f(n):
    if n == 1:
        return 1
    else:
        return n*f(n-1)


print(f(5))


def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]


print(rvs("abcde"))

count = 0


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, src)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)


hanoi(3, "A", "C", "B")
print(count)
