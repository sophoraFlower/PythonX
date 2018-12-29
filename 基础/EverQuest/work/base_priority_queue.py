# -*- coding: utf-8 -*-

import heapq


class PriorityQueue:
    # 初始化
    def __init__(self):
        self._queue = []
        self._index = 0

    # heappush首先会把元素查到列表的尾部，然后调用下面的函数调整元素到合适的位置
    # 元组在比较大小的时候，首先比较第一个元素，如果能够判断那么就直接根据第一个元素进行判断
    # 如果不能，就取下一个元素进行判断，依次类推。直到比较出结果或者一方没有元素了。
    def push(self, item, priority):
        # 把值加入堆中，（-priority, self._index, item）
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 返回（弹出）堆中最小值[-1]
        return heapq.heappop(self._queue)[-1]


# ！符号，这个只在format中有用
# 'Item({!r})'.format(self.name) 等价于 'Item(%r) % self.name'
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'), 1)  # [(-1, 1, Item('foo')]
q.push(Item('bar'), 5)  # [(-5, 0, Item('bar')), (-1, 1, Item('foo'))]
q.push(Item('spam'), 4)  # [(-5, 0, Item('bar')), (-1, 1, Item('foo')), (-4, 2, Item('spam'))]
q.push(Item('grok'), 1)  # [(-5, 0, Item('bar')), (-1, 1, Item('foo')), (-4, 2, Item('spam')), (-1, 3, Item('grok'))]
print('q.pop() > 5', q.pop())
print('q.pop() > 4: ', q.pop())
print('q.pop() > 1: ', q.pop())
print('q.pop() > 1: ', q.pop())
