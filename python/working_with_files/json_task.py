import json
# json_text = json.dumps(
#     {
#         'name': 'test',
#         'age': 15,
#         'bool': True,
#     }
# )
#
# dict_text = json.loads(json_text)
#
# print(json_text)
# print(dict_text)


with open('data.json', 'r') as file:
    data = json.loads(file.read())

    print(data)
    print(type(data))

    data['stack'] = 'Python'

    with open('data.json', 'w') as file_for_write:
        file_for_write.write(json.dumps(data))

