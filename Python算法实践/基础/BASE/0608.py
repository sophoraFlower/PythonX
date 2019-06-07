

def nums(list_):
    if len(list_) == 0:
        return 0
    else:
        return 1 + nums(list_[1:])


print(nums([1, 'mmm', 88, 'kko']))

