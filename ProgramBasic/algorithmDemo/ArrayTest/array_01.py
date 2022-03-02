from array import *

x = array('i', [5, 15, 25, 35, 45])
for i in x:
    print(i)

print("------------------")

print(x[2])

print("------------------")

x.insert(0, 0)
for i in x:
    print(i)

print("------------------")

x.append(55)
for i in x:
    print(i)

print("------------------")

x.remove(15)
for i in x:
    print(i)

print("------------------")

m = x.pop()
n = x.pop(0)
print("m = " + str(m) + ", n = " + str(n))
for i in x:
    print(i)

print("------------------")

# o = x.index(15)
p = x.index(25)
print("p = " + str(p))

print("------------------")

x[1] = 255
for i in x:
    print(i)
