import time
import threading


# 运行时间统计计时器
def time_count_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        # run time: 4.4875500202178955
        print('run time: {}'.format(end - start))
    return wrapper


@time_count_decorator
def CountDown(n):
    while n > 0:
        n -= 1


CountDown(100000000)

t = 100000000
t1 = threading.Thread(target=CountDown, args=[t // 2])
t2 = threading.Thread(target=CountDown, args=[t // 2])
t1.start()
t2.start()
# run time: 4.571465015411377
t1.join()
# run time: 4.570021152496338
t2.join()

