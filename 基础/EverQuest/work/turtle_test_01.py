# coding=utf-8

import turtle
import math


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)


if __name__ == '__main__':
    bob = turtle.Turtle()
    # turtle.mainloop()
    polygon(bob, 8, 60)
    circle(bob, 100)
    arc(bob, 66, 180)

