# 函数的嵌套
def func(message):
    def get_message():
        print('Got a message: {}'.format(message))
    return get_message()


# 闭包
def func_closure():
    def get_message(message):
        print('Got a message: {}'.format(message))
    return get_message


func('hello world')  # Got a message: hello world

send_message = func_closure()
send_message('hello world')  # Got a message: hello world
