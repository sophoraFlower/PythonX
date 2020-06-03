# my_func('hello world')


"""
def my_func(message):
    my_sub_func(message)


def my_sub_func(message):
    print(message)


my_func("hello world")
"""

"""
def factorial(input):
    if not isinstance(input, int):
        raise Exception('input must be an integer')
    if input < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)


# print(factorial("str"))
print(factorial(0))
print(factorial(1))
print(factorial(3))
"""


def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of


square = nth_power(2)
cube = nth_power(3)

print(square(6))
print(cube(3))
