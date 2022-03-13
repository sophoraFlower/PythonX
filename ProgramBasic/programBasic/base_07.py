class MyInputError(Exception):
    """Exception raised when there are errors in input"""

    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的string表达形式
        return "{} is invalid input".format(repr(self.value))


try:
    raise MyInputError(1)  # 抛出MyInputError这个异常
except MyInputError as err:
    print('error: {}'.format(err))


def factorial(input):
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * factorial(input - 1)

    return inner_factorial(input)


print(factorial(5))


def outer():
    x = "local"

    def inner():
        nonlocal x  # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)  # inner: nonlocal

    inner()
    print("outer:", x)  # outer: nonlocal


outer()


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of  # 返回值是exponent_of函数


# 外部函数 nth_power() 的参数 exponent，仍然会被内部函数 exponent_of() 记住
square = nth_power(2)
cube = nth_power(3)

print(square(6))  # 36
print(cube(6))  # 216
