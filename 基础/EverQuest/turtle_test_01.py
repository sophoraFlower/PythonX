# coding=utf-8

import turtle


def square(t, length, n):
    for i in range(8):
        t.fd(length)
        t.lt(360/n)


def circle(t, length, n):
    t.polygon(t, length, n)


bob = turtle.Turtle()
# turtle.mainloop()
# square(bob, 50, 8)
circle(bob, 60, 5)

