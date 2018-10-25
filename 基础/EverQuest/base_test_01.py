# coding=utf-8

import math


# 递归
def countdown(n):
    if n <= 0:
        print('end!')
    else:
        print(n)
        countdown(n-1)


# 返回值
def area(radius):
    a = math.pi * radius ** 2
    return a


# 增量式开发
def distance1(x1, y1, x2, y2):
    return 0.0


def distance2(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    print('dx is', dx)
    print('dx is', dy)
    return 0.0


def distance3(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    dsquared = dx ** 2 + dy ** 2
    print('dsquared is', dsquared)
    return 0.0


def distance4(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    dsquared = dx ** 2 + dy ** 2
    result = math.sqrt(dsquared)
    return result


# 组合
def circle_area(xc, yc, xp, yp):
    radius = distance4(xc, yc, xp, yp)
    result = area(radius)
    return result


# 简化
def circle_area_jh(xc, yc, xp, yp):
    return area(distance4(xc, yc, xp, yp))


# 布尔函数
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


def is_between(x, y, z):
    if x < y < z:
        return True
    else:
        return False


# 漩涡状
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * (n-1)
    return result


def factorialplus(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorialplus(n-1)


# 调试
def factorialdebug(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorialdebug(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result


if __name__ == '__main__':
    # countdown(6)
    # print(area(10))
    dis1 = distance1(5, 7, 8, 11)
    print(dis1)
    dis2 = distance2(5, 7, 8, 11)
    print(dis2)
    dis3 = distance3(5, 7, 8, 11)
    print(dis3)
    dis4 = distance4(5, 7, 8, 11)
    print(dis4)
    dis5 = circle_area_jh(5, 7, 8, 11)
    print(dis5)
    print(is_divisible(6, 6))
    print(is_divisible(3, 5))
    print(is_between(6, 7, 8))
    print(is_between(3, 5, 4))
    print(factorial(4))
    print(factorialplus('miaomaio'))
    print(factorialplus(-6))
    print(factorialplus(8))
    factorialdebug(8)


