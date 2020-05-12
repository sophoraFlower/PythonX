import math
import time
import random


# n >= 1 楼梯长度
def min_climb_stairs(n):
    # 可走一步或两步,求最小步数
    if n == 1 or n == 2:
        return 1
    else:
        return min_climb_stairs(n-2) + min_climb_stairs(1)


# n >= 1 楼梯长度
def climb_stairs(n):
    # 可走一步或两步,求路径数
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb_stairs(n-2) + climb_stairs(n-1)


def min_yinghe_climb_stairs(n):
    # 可走一步或两步,求路径数
    ax = 1  # 走一步的数量
    ways = []
    if n == 1:
        return 1
    else:
        while ax <= n:
            by = (n-ax)/2
            ways.append(math.ceil(ax+by))
            ax += 1
        return min(ways)


def yinghe_climb_stairs(n):
    # 爬台阶，可走一步或两步,求路径数
    ax = 1  # 走一步的数量
    ways = [1*random.randint(0, 2)+2*random.randint(0, 2)]
    # if n == 1:
    #     return 1
    # else:
    #     while ax <= n:
    #         by = (n-ax)/2
    #         ways.append(math.ceil(ax+by))
    #         ax += 1
    #     return min(ways)
    return ways


if __name__ == '__main__':
    start1_time = time.perf_counter()
    print(climb_stairs(5))
    end1_time = time.perf_counter()
    print(end1_time-start1_time)
    start2_time = time.perf_counter()
    print(yinghe_climb_stairs(4))
    end2_time = time.perf_counter()
    print(end2_time - start2_time)
