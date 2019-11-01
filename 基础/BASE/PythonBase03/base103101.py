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
"""

"""
def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                print('print warn log!')
            else:
                print('print other log!')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log(level='warn')
def foo(name, age=None, height=None):
    print('i am foo' + name)
    print('my age is %s, height %s' % (age, height))


# foo = log(foo)
foo('biubiubiu~~', 26, 172)
"""


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        print('class decorator running')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()
