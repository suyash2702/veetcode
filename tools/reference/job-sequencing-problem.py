def jobScheduling(deadlines, profits):
    jobs = sorted(zip(profits, deadlines), reverse=True)
    limit = max(deadlines)
    parent = list(range(limit + 1))

    def find(slot):
        while parent[slot] != slot:
            parent[slot] = parent[parent[slot]]
            slot = parent[slot]
        return slot

    done = total = 0
    for profit, deadline in jobs:
        slot = find(min(deadline, limit))
        if slot > 0:
            parent[slot] = slot - 1
            done += 1
            total += profit
    return [done, total]
