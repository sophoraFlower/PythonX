# coding=utf-8
import copy
'''
    type()
    isinstance()
    hasattr()
    AttributeError
'''


class Point:
    """Represents a point in 2-D space."""
    x = 0.0
    y = 0.0


class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """
    width = 0.0
    height = 0.0
    corner = {}


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


if __name__ == '__main__':
    # 实例
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 10.0
    box.corner.y = 10.0
    center = find_center(box)
    print_point(center)  # (60, 110)
    grow_rectangle(box, 50, 100)
    print(box.width, box.height)  # 150.0 300.0
    box1 = copy.copy(box)
    # box和 box1 拥有相同的数据，但是它们并不是同一个 Rectangle 对象
    print(box)
    print(box1)
    print(box is box1)  # False
    print(box == box1)  # False
    # 仅复制了对象以及其包含的引用， 但未复制嵌套的对象
    print(box.corner is box1.corner)   # True

    # deepcopy
    # 复制一个对象，还可以复制这个对象所引用的对象， 甚至可以复制这个对象所引用的对象所引用的对象
    box3 = copy.deepcopy(box)
    print(box3 is box)  # False
    print(box3.corner is box.corner)  # False
    print(box)
    print(box3)

