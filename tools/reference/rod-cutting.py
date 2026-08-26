def cutRod(prices):
    n = len(prices)
    best = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            best[length] = max(best[length], prices[cut - 1] + best[length - cut])
    return best[n]
