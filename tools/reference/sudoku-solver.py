def solveSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == ".":
                empty.append((r, c))
            else:
                rows[r].add(value)
                cols[c].add(value)
                boxes[(r // 3) * 3 + c // 3].add(value)

    def walk(index):
        if index == len(empty):
            return True
        r, c = empty[index]
        box = (r // 3) * 3 + c // 3
        for digit in "123456789":
            if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                continue
            board[r][c] = digit
            rows[r].add(digit)
            cols[c].add(digit)
            boxes[box].add(digit)
            if walk(index + 1):
                return True
            board[r][c] = "."
            rows[r].discard(digit)
            cols[c].discard(digit)
            boxes[box].discard(digit)
        return False

    walk(0)
    return board
