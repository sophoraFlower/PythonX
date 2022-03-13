from functools import reduce


def multiply_2(l):
    for index in range(0, len(l)):
        l[index] *= 2
    return l


def multiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item * 2)
    return new_list


l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
multiply_2(l1)
multiply_2(l1)
multiply_2(l1)
print(l1)    # [8, 16, 24, 32]
multiply_2_pure(l2)
multiply_2_pure(l2)
multiply_2_pure(l2)
print(l2)  # [1, 2, 3, 4]

l = [1, 2, 3, 4, 5]
new_list_map = map(lambda x: x * 2, l)  # [2， 4， 6， 8， 10]
new_list_filter = filter(lambda x: x % 2 == 0, l)  # [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, l)  # 1*2*3*4*5 = 120


