import heapq


def minMeetingRooms(intervals):
    rooms = []
    for start, end in sorted(intervals):
        if rooms and rooms[0] <= start:
            heapq.heapreplace(rooms, end)
        else:
            heapq.heappush(rooms, end)
    return len(rooms)
