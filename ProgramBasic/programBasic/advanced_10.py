def is_iterable(param_):
    try:
        iter(param_)
        return True
    except TypeError:
        return False


params = [1234,
          '1234',
          [1, 2, 3, 4],
          {1, 2, 3, 4},
          {1: 1, 2: 2, 3: 3, 4: 4},
          (1, 2, 3, 4)]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))
