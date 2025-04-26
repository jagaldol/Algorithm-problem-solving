import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(M)]


def sol():
    graph = [[] for _ in range(N + 1)]
    indegrees = [0] * (N + 1)

    for order in orders:
        for i in range(1, len(order) - 1):
            graph[order[i]].append(order[i + 1])
            indegrees[order[i + 1]] += 1

    queue = deque([i for i in range(1, N + 1) if indegrees[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for child in graph[node]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.append(child)

    if len(result) != N:
        print(0)
    else:
        print(*result)


sol()
