import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
dp = [[0, 1] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = [(1, False)]  # (현재 노드, 자식 처리가 끝났는지 여부)

while stack:
    node, processed = stack.pop()
    if not processed:
        visited[node] = True
        stack.append((node, True))  # 나중에 다시 처리
        for next_node in graph[node]:
            if not visited[next_node]:
                parent[next_node] = node
                stack.append((next_node, False))
    else:
        # 자식 정보가 다 채워졌으니 dp 갱신
        for child in graph[node]:
            if child == parent[node]:
                continue
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])

print(min(dp[1][0], dp[1][1]))