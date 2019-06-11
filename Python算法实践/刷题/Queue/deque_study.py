"""
    双端队列(或两端队列)具有从任一端添加和删除元素的功能。
    Deque模块是集合库的一部分。 它具有添加和删除可以直接用参数调用的元素的方法。
    在下面的程序中，将导入collections模块并声明一个双端队列。
    不需要任何类，直接使用内置的实现这些方法。
"""
import collections

DoubleEnded = collections.deque(["A", "B", "C"])
print(DoubleEnded)  # deque(['A', 'B', 'C'])

DoubleEnded.append("#")
DoubleEnded.appendleft("#")
print(DoubleEnded)  # deque(['#', 'A', 'B', 'C', '#'])

DoubleEnded.pop()
DoubleEnded.popleft()
print(DoubleEnded)  # deque(['A', 'B', 'C'])

DoubleEnded.reverse()
print(DoubleEnded)  # deque(['C', 'B', 'A'])



