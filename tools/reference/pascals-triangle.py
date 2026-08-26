def generate(numRows):
    out = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = out[i - 1][j - 1] + out[i - 1][j]
        out.append(row)
    return out
