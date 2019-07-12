# coding:utf8
import random

# 基本随机函数
print(random.seed(10))
for i in range(10):
    print(random.random())

# 扩展随机算法
print(random.randint(10, 100))
print(random.randrange(10, 100, 10))
print(random.getrandbits(16))
print(random.uniform(10, 20))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9]))
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(s)
print(s)
