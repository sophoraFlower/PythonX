# -*- coding: utf-8 -*-
import heapq

'''
    https://docs.python.org/3.7/library/heapq.html
'''
# heap[0] is the smallest item, and heap.sort() maintains the heap invariant!

list_0 = [9, 3, 4, -1, 8, 12]
list_1 = [6, 8, 1, 15]
print('list_0: ', list_0)

# heapify(x)
heapq.heapify(list_0)
print('heapify 》 list_0: ', list_0)

# heappush(heap, item)
heapq.heappush(list_0, 0)
print('heappush 0 》 list_0:', list_0)
heapq.heappush(list_0, 11)
print('heappush 11 》 list_0:', list_0)

# heappop(heap)
heapq.heappop(list_0)
print('heappop 》 list_0:', list_0)
heapq.heappop(list_0)
print('heappop 》 list_0:', list_0)

# heappushpop(heap, item)
heapq.heappushpop(list_0, 8)
print('heappushpop 8 》 list_0:', list_0)

# heapreplace(heap, item)
heapq.heapreplace(list_0, 5)
print('heapreplace 5 》 list_0:', list_0)

# merge(*iterables, key=None, reverse=False
heapq.heapify(list_0)
heapq.heapify(list_1)
list_2 = heapq.merge(list_0, list_1, key=None, reverse=False)
print(list_0)
print(list_1)
print(list_2)
merge_a, *merge_b = list_2
print('merge_a + *merge_b: ', (merge_a, *merge_b))

# nlargest(n, iterable, key=None)/nsmallest(n, iterable, key=None)
list_3 = list((merge_a, *merge_b))
print(heapq.nsmallest(3, list_3, key=None))
print(heapq.nlargest(3, list_3, key=None))


