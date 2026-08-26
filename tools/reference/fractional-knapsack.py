def fractionalKnapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda item: item[1] / item[0], reverse=True)
    total = 0.0
    left = capacity
    for weight, value in items:
        if left <= 0:
            break
        take = min(weight, left)
        total += value * take / weight
        left -= take
    return total
