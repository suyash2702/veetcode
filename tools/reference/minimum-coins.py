DENOMINATIONS = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]


def minimumCoins(amount):
    count = 0
    for note in DENOMINATIONS:
        if amount >= note:
            count += amount // note
            amount %= note
    return count
