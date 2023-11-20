str()  # to override type of value to string
int()  # to override type of value to integer
float()  # to override type of value to float
bool()  # to override type of value to boolean
type(None)  # return type of value as string


num_as_str = str(12)
num_as_int = int(num_as_str)
num_as_float = float(num_as_int)
bool_as_num = bool(0)

print(
    f'1) This is num_as_str: {num_as_str} - {type(num_as_str)}',
    f'2) This is num_as_str: {num_as_int} - {type(num_as_int)}',
    f'3) This is num_as_str: {num_as_float} - {type(num_as_float)}',
    f'4) This is num_as_str: {bool_as_num} - {type(bool_as_num)}',
    sep='\n'
)