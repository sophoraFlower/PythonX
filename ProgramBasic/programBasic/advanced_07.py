def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)
    return wrapper


def my_decorator_plus(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper


@my_decorator
def greet(message):
    print(message)


@my_decorator
def celebrate(name, message):
    print(name, message)


@my_decorator_plus
def celebrate2(name, message):
    print(name, message)


greet('hello world')  # wrapper of decorator \n hello world
celebrate('xx', 'hello world')  # TypeError: wrapper() takes 1 positional argument but 2 were given
celebrate2('xx', 'hello world')  # wrapper of decorator \n xx hello world
