num = 10


def sum_(n, i=0):

    if i == n + 1:
        return num

    if i % 2 == 0:
        print(i)

    return sum_(n, i + 1)


res = sum_(num)

