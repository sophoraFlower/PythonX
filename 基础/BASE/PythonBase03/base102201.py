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

