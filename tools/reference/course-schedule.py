from collections import deque


def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for course, need in prerequisites:
        graph[need].append(course)
        indegree[course] += 1
    queue = deque(i for i in range(numCourses) if indegree[i] == 0)
    seen = 0
    while queue:
        node = queue.popleft()
        seen += 1
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return seen == numCourses
