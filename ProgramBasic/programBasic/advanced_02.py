import copy

l1 = [1, 2, 3, 4]
l2 = list(l1)
print(l1 is l2)  # False

s1 = {1, 2, 3}
s2 = set(s1)
print(s1 is s2)  # False

l3 = l1[:]
print(l1 is l3)  # False

l4 = copy.copy(l1)
print(l1 is l4)  # False

# 特殊情况
t1 = (1, 2, 3)
t2 = t1[:]
print(t1 is t2)  # True


ll1 = [[1, 2], (30, 40)]
ll2 = copy.deepcopy(l1)

ll1.append(100)
print(ll1)  # [[1, 2], (30, 40), 100]
print(ll2)  # [1, 2, 3, 4]

ll1[0].append(3)
print(ll1)  # [[1, 2, 3], (30, 40), 100]
print(ll2)  # [1, 2, 3, 4]
