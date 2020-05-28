try:
    10 / 0
except (ZeroDivisionError, IndexError, InterruptedError) as err:
    print("ZeroDivision error:{}".format(err))

finally:
    print("other error")


class MyInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{} is invalid input".format(self.value)


try:
    raise MyInputError(1)
except MyInputError as err:
    print("error is {}".format(err))


"""
try:
    db = DB.connect('<db path>') # 可能会抛出异常
    raw_data = DB.queryData('<viewer_id>') # 可能会抛出异常
except (DBConnectionError, DBQueryDataError) err:
    print('Error: {}'.format(err))
"""