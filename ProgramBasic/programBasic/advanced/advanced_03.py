import copy
x = [1]
# 无限循环
x.append(x)
print(x)

y = copy.deepcopy(x)
print(y)

print(x == y)  # RecursionError: maximum recursion depth exceeded in comparison
print(x is y)  # False
