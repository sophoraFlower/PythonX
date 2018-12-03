# coding:utf-8


def quick_sort(array):
    # 基线条件
    if len(array) < 2:
        return array
    else:
        # 递归条件
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 编写求和函数
def sum_h(array):
    # 基线条件
    if len(array) < 2:
        return array[0]
    else:
        # 递归条件
        sum_base = array[0]
        arr_tail = array[1:]
        return sum_base + sum_h(arr_tail)


# 计算列表的包含数
def sum_n(array):
    n = 0
    # 基线条件
    if array:
        n += 1
        return n + sum_n(array[1:])
    else:
        return n


# 找出列表的最大数
def sum_m(array):
    # 基线条件
    if len(array) < 2:
        return array[0]
    else:
        # 递归条件
        list_max = array[0] if sum_m(array[1:]) < array[0] else sum_m(array[1:])
        return list_max


print(quick_sort([8, 2, 6, 9, 5, 12, 31, 1]))
print(sum_h([8, 2, 6, 9, 5, 12, 31, 1]))
print(sum_n([8, 2, 6, 9, 5, 12, 31, 1]))
print(sum_m([8, 2, 6, 9, 5, 12, 31, 1]))
