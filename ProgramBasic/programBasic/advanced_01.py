a, b = 30, 30
c, d = [2, 3], [2, 3]


print(a == b)  # True
print(id(a))
print(id(b))
print(a is b)  # True

print(c == d)  # True
print(id(c))
print(id(d))
print(c is d)  # False
