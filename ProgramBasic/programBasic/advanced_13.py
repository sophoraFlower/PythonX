def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)


print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))
