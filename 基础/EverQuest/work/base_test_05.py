# coding=utf-8

# 列表
# 映射、帅选和归并


def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


# 大多数的列表方法会对参数进行修改，然后返回None
letters = ['b', 'g', 'c', 'd']
le = letters.sort()
print(le)  # None
print(letters.sort())  # None
print(letters)  # ['b', 'c', 'd', 'g']

# 列表方法较多，选择一种写法即可
t = 'j'
# letters = ['b', 'c', 'd', 'g', 'j']
letters.append(t)
letters = letters + [t]
letters += [t]

# letters.append([t])          # 错误！
# letters = letters.append(t)  # 错误！
# letters + [t]                # 错误！
# letters = t + t              # 错误！

# 拷贝
letters2 = letters[:]  # 拷贝
letters2.sort()  # ['b', 'c', 'd', 'g', 'j']  # 改变原列表的排序
sorted(letters)  # ['b', 'c', 'd', 'g', 'j']  # 不改变原列表的排序，返回一个新的已排序的列表


# ---------------------------------------------------------------------------
# ---------------------------------- 字典 -----------------------------------
# 逆向查找
# raise 语句 能触发异常，这里它触发了 ValueError，这是一个表示查找操作失败的内建异常
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in the dictionary')


# 倒转字典
def invert_dict(df):
    inverse = dict()
    for key1 in df:
        val = df[key1]
        if val not in inverse:
            inverse[val] = [key1]
        else:
            inverse[val].append(key1)
    return inverse


d1 = {'a': 0, 'b': 1, 'c': 2, 'd': 1, 'e': 0}
print(invert_dict(d1))  # {0: ['a', 'e'], 1: ['b', 'd'], 2: ['c']}

# 全局变量
verbose = True


def example1():
    if verbose:
        print("Running example1")


# 元组
print((0, 1, 2) < (0, 3, 4))
print((0, 4, 2) < (0, 3, 4))
print((0, 4, 5) < (0, 3, 4))

# 值互换
a1 = 8
a2 = 7
(a1, a2) = (a2, a1)
print(a1)
print(a2)

# 内建函数 divmod 接受两个实参，返回包含两个值的元组：商和余数
t = divmod(7, 3)
print(t)


# 元组作为返回值
def min_max(x):
    return min(x), max(x)


# 列表和元组
# zip是一个内建函数，可以接受将两个或多个序列组，并返回一个元组列表， 其中每个元组
# 包含了各个序列中相对位置的一个元素

s = 'abc'
t = [0, 1, 2]
# zip对象是迭代器的一种
print(zip(s, t))  # <zip object at 0x0000009CB43DD448>
# 迭代器：任何能够按照某个序列迭代的对象。 迭代器在某些方面与列表非常相似，
# 但不同之处在于，你无法通过索引来选择迭代器中的某个元素


# 遍历两个列表
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


# 内建函数 enumerate
for index, element in enumerate('abc'):
    print(index, element)


# 字典和元组
d = {'a': 0, 'b': 1, 'c': 2}
t = d.items()
print(t)  # dict_items([('a', 0), ('b', 1), ('c', 2)])

for key, value in d.items():
    print(key, value)
# a 0
# b 1
# c 2

# dict和zip创建字典
dd = dict(zip('abc', range(3)))
print(dd)  # {'a': 0, 'b': 1, 'c': 2}


