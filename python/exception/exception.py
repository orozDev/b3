try:
    num = int(input())
    print(num)
except ValueError as error:
    print(type(error))
    print('Error!')
except KeyError as error:
    print('Key Error!')
finally:
    print('This the end')