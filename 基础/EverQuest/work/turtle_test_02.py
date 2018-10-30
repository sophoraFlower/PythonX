# coding=utf-8

import math
import turtle
import inspect


# 画正方形
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# 画多折线
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    stack = inspect.stack()
    the_class = stack[1][0].f_locals.__class__
    the_method = stack[1][0].f_code.co_name
    print("  polyline was called by {}.{}()".format(str(the_class), the_method))


# 画多边形
def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)


# 画弧
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)
    stack = inspect.stack()
    the_class = stack[1][0].f_locals.__class__
    the_method = stack[1][0].f_code.co_name
    print("  arc was called by {}.{}()".format(str(the_class), the_method))


# 画圆
def circle(t, r):
    arc(t, r, 360)


# 画花瓣
def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)
    stack = inspect.stack()
    the_class = stack[1][0].f_locals.__class__
    the_method = stack[1][0].f_code.co_name
    print("  petal was called by {}.{}()".format(str(the_class), the_method))


# 画花
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)
    stack = inspect.stack()
    the_class = stack[1][0].f_locals.__class__
    the_method = stack[1][0].f_code.co_name
    print("  flower was called by {}.{}()".format(str(the_class), the_method))


# 笔头移动
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
    stack = inspect.stack()
    the_class = stack[1][0].f_locals.__class__
    the_method = stack[1][0].f_code.co_name
    print("  move was called by {}.{}()".format(str(the_class), the_method))


if __name__ == '__main__':
    bob = turtle.Turtle()
    # square(bob, 100)
    # 画折现
    # polyline(bob, 6, 120, 45)
    # 画正八边形
    # polygon(bob, 8, 140)
    # 画弧形
    # arc(bob, 80, 270)
    # 画圆
    # circle(bob, 100)
    # 画花瓣
    # petal(bob, 100, 80)
    # 画六瓣花
    # flower(bob, 6, 80, 45)
    # move(bob, 50)
    move(bob, -100)
    flower(bob, 7, 60.0, 60.0)

    move(bob, 100)
    flower(bob, 10, 40.0, 80.0)

    move(bob, 100)
    flower(bob, 20, 140.0, 20.0)

    bob.hideturtle()
    turtle.mainloop()

