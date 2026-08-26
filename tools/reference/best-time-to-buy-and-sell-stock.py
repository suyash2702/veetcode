def maxProfit(prices):
    best = 0
    low = float('inf')
    for p in prices:
        low = min(low, p)
        best = max(best, p - low)
    return best
