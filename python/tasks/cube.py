cubes_count = int(input('Введите количество кубиков: '))
steps_count = 0
j = 0
while steps_count < cubes_count:
    steps_count += j
    j += 1
    print(f'j = {j}; steps_count = {steps_count}')

print(f'Result: {j - 1}')