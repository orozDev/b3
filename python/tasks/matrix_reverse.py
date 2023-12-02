matrix = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

reversed_matrix = []

for i in range(len(matrix)):
    reversed_matrix.append([])
    for j in range(len(matrix[i])):
        reversed_matrix[i].append(matrix[j][i])

for i in range(len(reversed_matrix)):
    print(*reversed_matrix[i], sep=' ')
