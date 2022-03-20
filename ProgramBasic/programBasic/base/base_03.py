s = 'a\nb\tc'
print(s)
print(len(s))  # 5

name = input('your name?：')
gender = input('you are a boy?(y/n)')

welcome_str = 'Welcome to the matrix {prefix} {name}'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs.',
    'name': name
}

print('authorizing......')
print(welcome_str.format(**welcome_dic))
