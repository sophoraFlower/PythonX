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


print(quick_sort([8, 2, 6, 9, 5, 12, 31, 1]))

