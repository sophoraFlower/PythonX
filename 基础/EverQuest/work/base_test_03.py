# coding=utf-8


def nested_sum(li):
    sums = 0
    for i in li:
        for j in i:
            sums += j
    return sums


def cumsum(li):
    sums = 0
    newsum = []
    for i in li:
        sums += i
        newsum.append(sums)
    return newsum


def middle(li):
    del li[0]
    del li[-1]
    return li


def chop(li):
    del li[0]
    del li[-1]


def is_sorted(li):
    sortli = sorted(li)
    n = 0
    for i in sortli:
        if li[n] == i:
            n = n + 1
            continue
        else:
            return False
    return True


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)


def has_duplications(li):
    li = sorted(li)
    n = 0
    for i in li[:-1]:
        if i == li[n+1]:
            return True
        else:
            n = n + 1
            continue
    return False


if __name__ == '__main__':
    t1 = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t1))
    t2 = [1, 2, 3]
    print(cumsum(t2))
    t3 = [1, 2, 3, 4]
    print(middle(t3))
    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))
    print(is_anagram('adfcb', 'abcfd'))
    print(is_anagram('adfcb', 'abcfde'))
    print(has_duplications(['a', 'b', 'k', 'l', 'd']))
    print(has_duplications(['a', 'b', 'k', 'l', 'd', 'b']))



