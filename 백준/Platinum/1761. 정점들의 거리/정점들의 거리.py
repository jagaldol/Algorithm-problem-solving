import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())


graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

LOG = 16  # 2^16 = 65536 > 40000
dist = [0] * (N + 1)
visited = [False] * (N + 1)
depth = [0] * (N + 1)
parent = [[0] * (LOG + 1) for _ in range(N + 1)]


def dfs(node):
    visited[node] = True
    for v, cost in graph[node]:
        if not visited[v]:
            depth[v] = depth[node] + 1
            parent[v][0] = node
            dist[v] = dist[node] + cost
            dfs(v)


dfs(1)

for j in range(1, LOG + 1):
    for i in range(1, N + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1]


def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u

    for j in range(LOG, -1, -1):
        if depth[u] - (1 << j) >= depth[v]:
            u = parent[u][j]

    if u == v:
        return u

    for j in range(LOG, -1, -1):
        if parent[u][j] != 0 and parent[u][j] != parent[v][j]:
            u = parent[u][j]
            v = parent[v][j]

    return parent[u][0]


M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(dist[u] + dist[v] - 2 * dist[lca(u, v)])
