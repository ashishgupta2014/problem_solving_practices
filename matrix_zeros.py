def setZeroes(matrix):
    rows, columns = [], []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                columns.append(j)

    while rows or columns:
        row = rows.pop()
        column = columns.pop()
        for i in range(len(matrix)):
            matrix[i][column] = 0
        for j in range(len(matrix[0])):
            matrix[row][j] = 0
