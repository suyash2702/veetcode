def floodFill(image, sr, sc, color):
    start = image[sr][sc]
    if start == color:
        return image
    rows, cols = len(image), len(image[0])
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != start:
            continue
        image[r][c] = color
        stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
    return image
