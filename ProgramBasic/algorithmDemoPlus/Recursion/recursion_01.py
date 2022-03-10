# coding=utf-8
import functools
import timeit


def time_of_climb_the_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 总的上楼梯次数等于还剩1阶台阶的走法次数和还剩2阶台阶的走法次数相加
    return time_of_climb_the_stairs(n - 1) + time_of_climb_the_stairs(n - 2)


# 内置装饰器，避免重复计算
@functools.lru_cache()
def time_of_climb_the_stairs_plus(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 总的上楼梯次数等于还剩1阶台阶的走法次数和还剩2阶台阶的走法次数相加
    return time_of_climb_the_stairs_plus(n - 1) + time_of_climb_the_stairs_plus(n - 2)


# 采用非递归的方式：循环迭代
def time_of_climb_the_stairs_loop(n):
    step1 = 1
    step2 = 2
    total = 0
    for step in range(2, n):
        total = step1 + step2
        step2, step1 = total, step2
    return total


start = timeit.default_timer()
times01 = time_of_climb_the_stairs(30)
end = timeit.default_timer()
print(times01)
print('Running time: %s Seconds', (end - start))

start = timeit.default_timer()
times02 = time_of_climb_the_stairs_plus(30)
end = timeit.default_timer()
print(times02)
print('Running time: %s Seconds', (end - start))

start = timeit.default_timer()
times03 = time_of_climb_the_stairs_loop(30)
end = timeit.default_timer()
print(times03)
print('Running time: %s Seconds', (end - start))
