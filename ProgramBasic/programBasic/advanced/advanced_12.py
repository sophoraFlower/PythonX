def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1


gen_1 = generator(1)
print(gen_1)  # <generator object generator at 0x1011310b0>

gen_3 = generator(3)
print(gen_3)  # <generator object generator at 0x1011310b0>

'''
for j in gen_1:
    if j < 10:
        print(j)  # 1, 2, 3, 4, 5, 6, 7, 8, 9

for j in gen_3:
    if j < 10:
        print(j)  # 1, 8
'''


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)


get_sum(8)


test_01 = generator(1)


def add(n):
    sum_ = 0
    for i in range(n):
        add_01 = next(test_01)
        sum_ += add_01
    return sum_


print(add(6))
