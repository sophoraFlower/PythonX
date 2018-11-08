# coding=utf-8

import copy
import math


# 类和对象
class Point:
    """Represents a point in 2-D space."""


blank = Point()
print(Point)  # <class '__main__.Point'>
# 返回值是一个Point对象的引用
print(blank)  # <__main__.Point object at 0x0000004F82319438>

blank.x = 3.0
blank.y = 4.0

print('(%g, %g)' % (blank.x, blank.y))  # (3, 4)


class Rectangle:
    """Represents a rectangle.
       attributes: width, height, corner.
    """


def print_point(p):
    print('(%g, %g)' % (p.m, p.n))


# 实例作为返回值
def find_center(rect):
    p = Point()
    p.m = rect.corner.m + rect.width/2
    p.n = rect.corner.n + rect.height/2
    return p


def distance_between_points(a1, a2):
    length = math.sqrt((a1.x - a2.x)**2 + (a1.y - a2.y)**2)
    return length


p1 = Point()
p2 = Point()
p1.x = 3
p1.y = 0
p2.x = 0
p2.y = 4
print("#### " + str(distance_between_points(p1, p2)))


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.m = 0.0
box.corner.n = 0.0

center = find_center(box)
print_point(center)

# 复制
blank2 = copy.copy(blank)
print('(%g, %g)' % (blank2.x, blank2.y))  # (3, 4)

print(blank2 is blank)
print(blank2 == blank)

# 浅复制--深复制

# 访问一个不存在的属性，你会得到 Attributeerror 的错误提示
# type()、isinstance(p, Point)
# 确定一个对象是否拥有某个属性-使用内置函数 hasattr 检查
print(hasattr(blank, 'x'))  # True
print(hasattr(blank, 'z'))  # False
