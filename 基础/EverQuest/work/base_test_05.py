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
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


d1 = {'a': 0, 'b': 1, 'c': 2, 'd': 1, 'e': 0}
print(invert_dict(d1))  # {0: ['a', 'e'], 1: ['b', 'd'], 2: ['c']}

# 全局变量
verbose = True


def example1():
    if verbose:
        print("Running example1")






