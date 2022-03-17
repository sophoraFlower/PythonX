import threading
import dis

n = 0


def foo():
    global n
    n += 1


threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

for i in range(20):
    print(n)
dis.dis(foo)
