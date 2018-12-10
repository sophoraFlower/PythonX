# coding: utf-8
import collections
import timeit

'''
    学习参考自：https://github.com/keon/algorithms
'''


# Time complexity O(n^2)
def delete_nth_naive(array, n):
    ans = []
    for num in array:
        # 每次判断执行O(n)
        if ans.count(num) < n:
            ans.append(num)
    return ans


# O(n)
def delete_nth(array, n):
    result = []
    # collections.defaultdict 类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值
    # 只有在通过dict[key]或者dict.__getitem__(key)访问的时候才有效
    counts = collections.defaultdict(int)  # keep track of occurrences

    for i in array:
        # 每次判断执行O(1)
        if counts[i] < n:
            result.append(i)
            counts[i] += 1
    return result


print(delete_nth([1, 2, 3, 4, 2, 1, 4, 6, 3, 4, 8, 9, 7, 3, 5, 4, 2, 2, 6, 1, 3], 3))
t1 = timeit.repeat("delete_nth_naive([1, 2, 3, 4, 2, 1, 4, 6, 3, 4, 8, 9, 7, 3, 5, 4, 2, 2, 6, 1, 3], 3)",
                   "from __main__ import delete_nth_naive", repeat=5, number=1000)
t2 = timeit.repeat("delete_nth([1, 2, 3, 4, 2, 1, 4, 6, 3, 4, 8, 9, 7, 3, 5, 4, 2, 2, 6, 1, 3], 3)",
                   "from __main__ import delete_nth", repeat=5, number=1000)
print(t1)  # [0.005722464999999954, 0.005449140999999991, 0.005385623000000006, 0.005015096999999968, 0.005900189]
print(t2)  # [0.005145342999999969, 0.005738505999999977, 0.004842184999999999, 0.005266926000000005, 0.00483031999974]
