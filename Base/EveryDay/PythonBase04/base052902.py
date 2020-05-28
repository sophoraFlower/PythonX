x = [-3, -2, -1, 0, 1, 2, 3]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)

text = ' Today, is, SUNDAY'
text_list = [s.strip() for s in text.split(',') if len(s.strip()) >= 5]
print(text_list)

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
          ['mike', '1999-01-01', 'male'],
          ['nancy', '2001-02-01', 'female']
          ]
"""
# expected output:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, 
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, 
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
"""

list_output = list()
for value in values:
    dict_output = dict()
    for i, attr in enumerate(attributes):
        dict_output[attr] = value[i]
    print(dict_output)
    list_output.append(dict_output)
print(list_output)

list_output_new = [{attr: value[index] for index, attr in enumerate(attributes)} for value in values]
print(list_output_new)
