import math
import time


# n >= 1 楼梯长度
def min_climb_stairs(n):
    # 可走一步或两步,求最小步数
    if n == 1 or n == 2:
        return 1
    else:
        return min_climb_stairs(n-2) + min_climb_stairs(1)


def yinghe_climb_stairs(n):
    # 可走一步或两步,求最小步数
    ax = 0  # 走一步的数量
    ways = []
    if n == 1:
        return 1
    else:
        while ax <= n:
            by = (n-ax)/2
            ways.append(math.ceil(ax+by))
            ax += 1
        return min(ways)


if __name__ == '__main__':
    start1_time = time.perf_counter()
    print(min_climb_stairs(1001))
    end1_time = time.perf_counter()
    print(end1_time-start1_time)
    start2_time = time.perf_counter()
    print(yinghe_climb_stairs(1001))
    end2_time = time.perf_counter()
    print(end2_time - start2_time)
