# -*- coding: utf-8 -*-

import heapq


class PriorityQueue:
    # 初始化
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)  # [(-5, 0, Item('bar')), (-1, 1, Item('foo')), (-4, 2, Item('spam')), (-1, 3, Item('grok'))]
print('q.pop() > 5', q.pop())
print('q.pop() > 4: ', q.pop())
print('q.pop() > 1: ', q.pop())
print('q.pop() > 1: ', q.pop())
