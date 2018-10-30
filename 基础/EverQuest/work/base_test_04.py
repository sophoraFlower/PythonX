# coding=utf-8


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogramjj(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


if __name__ == '__main__':
    h1 = histogram('brontosaurus')
    print(h1)
    h2 = histogramjj('brontosaurus')
    print(h2)
    h3 = histogram('parrot')
    print_hist(h3)

