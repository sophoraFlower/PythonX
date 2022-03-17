import sys
import threading

a = []
b = a


def item():
    c = a
    print(sys.getrefcount(c))  # 4


t = threading.Thread(target=item)
# a 的引用计数是 3
print(sys.getrefcount(a))  # 3
print(sys.getrefcount(b))  # 3

t.start()
t.join()

