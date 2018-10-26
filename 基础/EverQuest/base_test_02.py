# coding=utf-8

import sys
import math
sys.setrecursionlimit(1000000)
epsilon = 0.00001


def mysqrt(n):
    x = n / 2
    y = (x + n / x) / 2
    while True:
        if abs(y-x) < epsilon:
            return y
        else:
            x = y
            y = (x + n / x) / 2


def test_squre_root(n):
    print("a   mysqrt(a)    math.sqrt(a)    diff")
    print("-   ---------    ------------    ----")
    m = 1.0
    while True:
        if m == n + 1:
            break
        else:
            print('{0}   {1}    {2}    {3}'.format(m, mysqrt(m), math.sqrt(m), abs(math.sqrt(m)-mysqrt(m))))
            m = m + 1.0


def eval_loop():
    ip = input("input:")
    while True:
        if ip == 'done':
            break
        else:
            print(eval(ip))
            ip = input("input:")


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)-1

    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True


# test_squre_root(9)
# eval_loop()
print(is_reverse('abcdef', 'fedcba'))
print(is_reverse('abcdef', 'fedbba'))
