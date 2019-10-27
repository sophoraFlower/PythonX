import copy
"""
a = [1]
b = [1]
print(a == b)    # True
print(a is b)    # False

t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])
print(t1 == t2)    # True
print(t1 is t2)    # False

t1[-1].append(5)
print(t1 == t2)    # False
"""
"""
l1 = [[1, 2], (30, 40)]
# 深度拷贝
l2 = copy.deepcopy(l1)
l1.append(100)
l1[0].append(3)

print(l1)  # [[1, 2, 3], (30, 40), 100]
print(l2)  # [[1, 2], (30, 40)]

l3 = copy.copy(l1)
l3[1] += (50,)
print(l1)  # [[1, 2, 3], (30, 40), 100]
print(l3)  # [[1, 2, 3], (30, 40, 50), 100]
l3[0].append(4)
print(l1)  # [[1, 2, 3, 4], (30, 40), 100]
print(l2)  # [[1, 2], (30, 40)]
print(l3)  # [[1, 2, 3, 4], (30, 40, 50), 100]
"""

x = [1]
x.append(x)
print(x)  # [1, [...]]
x = copy.copy(x)
print(x)

y = copy.deepcopy(x)
print(y)  # [1]
