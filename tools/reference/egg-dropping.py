def eggDrop(eggs, floors):
    # covered[e] = floors distinguishable with e eggs and the current number of drops
    covered = [0] * (eggs + 1)
    drops = 0
    while covered[eggs] < floors:
        drops += 1
        for e in range(eggs, 0, -1):
            covered[e] = covered[e] + covered[e - 1] + 1
    return drops
