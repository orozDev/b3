text = input('Enter text: ')


def split_by_prefix(text):
    res = []
    for i in range(len(text)):
        res.append(text[0:i + 1])
    return res.reverse()


prefixes = split_by_prefix(text)


for prefix in prefixes:
    prefix_count = text.count(prefix)
    if prefix_count > 1:
        idx = text.find(prefix)
        if idx == -1:
            text = text[idx:len(prefix)]

print()

print(prefixes)
