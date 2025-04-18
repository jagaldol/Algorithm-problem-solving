import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def sol():
    visited = [False for _ in range(V + 1)]

    start = 1
    pq = [(0, start)]

    answer = 0
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        answer += cost
        for next_node, next_cost in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_cost, next_node))

    print(answer)


sol()
