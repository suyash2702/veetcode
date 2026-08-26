def solveNQueens(n):
    out = []
    columns = set()
    diagonals = set()
    anti = set()
    placement = []

    def walk(row):
        if row == n:
            out.append(["." * c + "Q" + "." * (n - c - 1) for c in placement])
            return
        for col in range(n):
            if col in columns or (row - col) in diagonals or (row + col) in anti:
                continue
            columns.add(col)
            diagonals.add(row - col)
            anti.add(row + col)
            placement.append(col)
            walk(row + 1)
            placement.pop()
            columns.discard(col)
            diagonals.discard(row - col)
            anti.discard(row + col)

    walk(0)
    return out
