import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    a_ = [i for i in range(10000000)]
    show_memory_info('after a created')


func()
show_memory_info('finished')


def func2():
    show_memory_info('initial')
    global al
    al = [i for i in range(10000000)]
    show_memory_info('after a created')


func2()
show_memory_info('finished')


def func3():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')
    return a


a = func3()
show_memory_info('finished')
