import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input())
LOG = 21  # 2^20 = 1,048,576 > 10^5

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[0] * LOG for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)


def dfs(node, d):
    visited[node] = True
    depth[node] = d
    for next_node in graph[node]:
        if not visited[next_node]:
            parent[next_node][0] = node
            dfs(next_node, d + 1)


dfs(1, 0)

# Binary lifting
for j in range(1, LOG):
    for i in range(1, N + 1):
        parent[i][j] = parent[parent[i][j - 1]][j - 1]


def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    # 높이 맞추기
    for i in reversed(range(LOG)):
        if depth[u] - depth[v] >= (1 << i):
            u = parent[u][i]
    if u == v:
        return u
    # 동시에 점프
    for i in reversed(range(LOG)):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]
    return parent[u][0]


M = int(input())
for _ in range(M):
    u, v = map(int, input().split())
    print(lca(u, v))
