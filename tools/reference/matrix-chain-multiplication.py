def matrixMultiplication(dims):
    n = len(dims)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = min(
                dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                for k in range(i, j)
            )
    return dp[1][n - 1] if n > 2 else 0
