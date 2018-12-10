# coding: utf-8
from collections import Iterable
import timeit

'''
    学习参考自：https://github.com/keon/algorithms
'''

"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""


# return list
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)    # tail-recursion
        else:
            output_arr.append(ele)      # produce the result
    return output_arr


# returns iterator
# 递归思想实现数组降维，返回generator, 好处惰性加载，节约内存
# python默认最大递归次数为1000，所以数组维数过大时会抛出 maximum recursion depth exceeded while calling a Python object 错误
# 使用sys模块的sys.setrecursionlimit(1500)可以设置最大递归次数
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten_iter(element)
        else:
            yield element


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(flatten_iter([[1, 2, 3, 4], [[5, 6], [7, 8, 9]], 10])))
print(flatten([[1, 2, 3, 4], [[5, 6], [7, 8, 9]], 10]))

t1 = timeit.timeit("flatten([[1, 2, 3, 4], [[5, 6], [7, 8, 9]], 10])", "from __main__ import flatten",
                   number=1000)
t2 = timeit.timeit("flatten_iter([[1, 2, 3, 4], [[5, 6], [7, 8, 9]], 10])", "from __main__ import flatten_iter",
                   number=1000)
print(t1)  # 0.006128921000000009
print(t2)  # 0.00034646600000004524