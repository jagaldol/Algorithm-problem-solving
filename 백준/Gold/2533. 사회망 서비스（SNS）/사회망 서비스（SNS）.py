import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
visited = [False] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    degree[u] += 1
    degree[v] += 1


def sol():
    q = deque([i for i in range(1, n + 1) if degree[i] == 1])

    result = 0

    while q:
        node = q.popleft()
        visited[node] = True
        for parent in graph[node]:
            if visited[parent]:
                continue
            result += 1  # 부모를 얼리 어답터로 선택
            visited[parent] = True
            for grand in graph[parent]:
                degree[grand] -= 1
                if not visited[grand] and degree[grand] == 1:
                    q.append(grand)
            break  # 부모 한 명만 선택하면 충분함

    print(result)


sol()
