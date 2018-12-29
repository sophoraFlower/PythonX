# coding: utf-8

from collections import defaultdict
from collections import OrderedDict
import json

# defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(2)
print("a: {0[a]}, b: {0[b]}".format(d))  # a: [1, 2, 3], b: [2]

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print("a: {0[a]}, b: {0[b]}".format(d))  # a: {1, 2}, b: {4}

d = {}  # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print("a: {0[a]}, b: {0[b]}".format(d))  # a: [1, 2], b: [4]

# pairs = {}
# # 创建一个多值映射字典,基础实现
# d = {'c': 0, 'c': 1, 'c': 2, 'd': 1, 'd': 2}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)
# print("c: {0[c]}, d: {0[d]}".format(d))
# # 使用defaultdict
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

print(json.dumps(d))  # {"foo": 1, "bar": 2, "spam": 3, "grok": 4}

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)  # (612.78, 'AAPL')
print(min_price)  # (10.75, 'FB')

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)  # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]


