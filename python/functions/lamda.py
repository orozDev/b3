def is_even(num):
    return num % 2 == 0

is_even2 = lambda num: num % 2 == 0

res = is_even(12)
res2 = is_even2(12)

print(res, res2)