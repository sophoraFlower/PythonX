import functools
"""
def my_decorator(func):
    # 函数 my_decorator() 就是一个装饰器，它把真正需要执行的函数 greet() 包裹在其中
    # 并且改变了它的行为，但是原函数 greet() 不变
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


@my_decorator
def greet():
    print('hello world')


# greet = my_decorator(greet)
greet()
"""

"""
def log(func):
    def wrapper(*args, **kw):
        print('call '+func.__name__+'()')
        return func(*args, **kw)
    return wrapper()


@log
def now():
    print('2019-10-31')


print(now())
"""

"""
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2019-10-31')
"""


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('biubiubiu....')
def now():
    print('2019-10-31')


now()


