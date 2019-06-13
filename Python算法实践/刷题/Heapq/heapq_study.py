"""
heapify - 此函数将常规列表转换为堆。 在结果堆中，最小的元素被推到索引位置0。但是其余的数据元素不一定被排序。
heappush - 这个函数在堆中添加一个元素而不改变当前堆。
heappop - 该函数返回堆中最小的数据元素。
heapreplace - 该函数用函数中提供的新值替换最小的数据元素。
"""
import heapq

H = [5, 12, 4, 33, 55]
heapq.heapify(H)
print(H)
heapq.heappush(H, 8)
print(H)
print(heapq.heappop(H))
heapq.heapreplace(H, 18)
print(H)
