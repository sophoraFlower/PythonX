import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4, 'amount': 23
}

params_str = json.dumps(params)
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))
# type of params_str = <class 'str'>, params_str = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
original_params = json.loads(params_str)
print(('type of original_params = {}, original_params = {}'.format(type(original_params), original_params)))
# type of original_params = <class 'dict'>, original_params = {'symbol': '123456', 'type': 'limit', 'price': 123.4, 'amount': 23}
