# 简单装饰器的实现
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


def greet():
    print('hello world')


@my_decorator
def greet2():
    print('hello world')


todo = my_decorator(greet)
todo()  # wrapper of decorator \n hello world

greet2()  # wrapper of decorator \n hello world
