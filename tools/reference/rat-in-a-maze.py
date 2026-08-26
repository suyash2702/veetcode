def findPaths(maze):
    n = len(maze)
    if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []

    out = []
    path = []
    moves = (("D", 1, 0), ("L", 0, -1), ("R", 0, 1), ("U", -1, 0))

    def walk(r, c):
        if r == n - 1 and c == n - 1:
            out.append("".join(path))
            return
        maze[r][c] = 0
        for name, dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1:
                path.append(name)
                walk(nr, nc)
                path.pop()
        maze[r][c] = 1

    walk(0, 0)
    return out
