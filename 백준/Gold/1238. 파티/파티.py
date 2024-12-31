import heapq
import sys

input = sys.stdin.readline
INF = 1_000_000_000
N, M, X = map(int, input().split())
costs = [[INF if i != j else 0 for i in range(N + 1)] for j in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    costs[s][e] = t

results = [0 for _ in range(N + 1)]


def dijkstra(backward=False):
    visited = [False for _ in range(N + 1)]
    pq = []
    heapq.heappush(pq, (0, X))
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        results[node] += cost
        for i in range(1, N + 1):
            next_cost = costs[i][node] if backward else costs[node][i]
            if next_cost != INF and not visited[i]:
                heapq.heappush(pq, (cost + next_cost, i))


def sol():
    dijkstra()
    dijkstra(True)
    print(max(results))


sol()
