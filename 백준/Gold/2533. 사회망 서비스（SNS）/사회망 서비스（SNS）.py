import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
dp = [[0, 1] for _ in range(N + 1)]


def recursive(node):
    if visited[node]:
        return
    visited[node] = 1
    for node2 in graph[node]:
        if visited[node2]:
            continue
        recursive(node2)
        dp[node][0] += dp[node2][1]
        dp[node][1] += min(dp[node2][0], dp[node2][1])


recursive(1)
print(min(dp[1][0], dp[1][1]))
