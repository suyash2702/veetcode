def floydWarshall(matrix):
    n = len(matrix)
    INF = float("inf")
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = INF
    for k in range(n):
        row_k = matrix[k]
        for i in range(n):
            via = matrix[i][k]
            if via == INF:
                continue
            row_i = matrix[i]
            for j in range(n):
                if via + row_k[j] < row_i[j]:
                    row_i[j] = via + row_k[j]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == INF:
                matrix[i][j] = -1
    return matrix
