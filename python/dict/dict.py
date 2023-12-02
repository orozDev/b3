staff = {
    'name': 'Badalov Nurullo',
    'age': 20,
    'experience': 1
}

name = staff['name']
staff['height'] = 168
staff.setdefault('role', 'tester')
staff['weight'] = 67

print(staff.get('weight', 78))
print('Staff as dict:', staff)

# print(list(staff.values()))

staff.update({'salary': 15000})

print('\nStaff values:')
for val in staff.values():
    print(val)

print('\nStaff keys:')
for key in staff.keys():
    print(key)


res = staff.pop('salary', 60000)

print(f'res: {res}')


print('\nStaff keys and vals:')
for key, val in staff.items():
    print(f'{key}: {val}')