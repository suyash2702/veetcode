MASK = 0xFFFFFFFF


def getSum(a, b):
    a &= MASK
    b &= MASK
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a < 0x80000000 else a - (MASK + 1)
