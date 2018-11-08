# coding=utf-8


class Time:
    hour = 0
    minute = 0
    second = 0


def print_time(timex):
    print("%.2d:%.2d:%.2d" % (timex.hour, timex.minute, timex.second))


def is_after(time1, time2):
    return (time1.hour, time1.minute, time1.second) < (time2.hour, time2.minute, time2.second)


# def add_time(t1, t2):
#     sum = Time()
#     sum.hour = t1.hour + t2.hour
#     sum.minute = t1.minute + t2.minute
#     sum.second = t1.second + t2.second
#     return sum


def add_time(time1, time2):
    sumt = Time()
    sumt.hour = time1.hour + time2.hour
    sumt.minute = time1.minute + time2.minute
    sumt.second = time1.second + time2.second

    if sumt.second >= 60:
        sumt.second -= 60
        sumt.minute += 1
    if sumt.minute >= 60:
        sumt.minute -= 60
        sumt.hour += 1
    return sumt


t = Time()
t.hour = 9
t.minute = 9
t.second = 19
print_time(t)
t1 = Time()
t1.hour = 9
t1.minute = 9
t1.second = 19
t2 = Time()
t2.hour = 9
t2.minute = 9
t2.second = 18
print(is_after(t1, t2))  # False


# 修改器：用函数修改作为参数传入的对象
def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


t3 = Time()
t3.hour = 9
t3.minute = 9
t3.second = 9
increment(t3, 60)
print_time(t3)  # 09:10:09


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time_plus(time_a, time_b):
    seconds = time_to_int(time_a) + time_to_int(time_b)
    return int_to_time(seconds)


def increment_plus(time_a, second_a):
    seconds = time_to_int(time_a) + second_a
    return int_to_time(seconds)


increment_plus(t3, 60)
print(t3)


# 调试
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time_debug1(tt1, tt2):
    if not valid_time(tt1) or not valid_time(tt2):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(tt1) + time_to_int(tt2)
    return int_to_time(seconds)


# 使用 assert语句，检查一个给定的不变式并在失败的情况下抛出异常
def add_time_debug2(tt1, tt2):
    assert valid_time(tt1) and valid_time(tt2)
    seconds = time_to_int(tt1) + time_to_int(tt2)
    return int_to_time(seconds)
