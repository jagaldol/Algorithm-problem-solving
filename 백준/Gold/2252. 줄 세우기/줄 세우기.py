import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degrees = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degrees[b] += 1


def sol():
    queue = deque([i for i in range(1, N + 1) if in_degrees[i] == 0])

    answer = []
    while queue:
        node = queue.popleft()
        answer.append(node)
        for child in graph[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                queue.append(child)

    print(*answer)


sol()
