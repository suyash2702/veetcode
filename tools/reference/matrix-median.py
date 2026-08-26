import bisect


def matrixMedian(matrix):
    rows, cols = len(matrix), len(matrix[0])
    half = (rows * cols) // 2
    lo = min(row[0] for row in matrix)
    hi = max(row[-1] for row in matrix)
    while lo < hi:
        mid = (lo + hi) // 2
        count = sum(bisect.bisect_right(row, mid) for row in matrix)
        if count <= half:
            lo = mid + 1
        else:
            hi = mid
    return lo
