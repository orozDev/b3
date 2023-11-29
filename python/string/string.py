name = 'python is the most popular pr language'

def concat(val, start = 0, end = None, step = 1):
    res = ''
    if end is None:
        end = len(val)
    for i in range(start, end, step):
        res += val[i]

    return res

print( name[0 : : 2] )
print( concat(name, 0, 6) )