import heapq

INF = 1_000_000_000


def dijkstra(costs, n, s):
    result = [INF if i != s else 0 for i in range(n + 1)]
    visited = [False if i != s else True for i in range(n + 1)]
    pq = []

    for i in range(1, n + 1):
        if costs[s][i] != INF:
            heapq.heappush(pq, (costs[s][i], i))

    while len(pq) > 0:
        cost, city = heapq.heappop(pq)
        if visited[city]:
            continue

        visited[city] = True
        result[city] = cost

        for i in range(1, n + 1):
            if not visited[i] and costs[city][i] != INF:
                heapq.heappush(pq, (cost + costs[city][i], i))

    return result


def solution(n, s, a, b, fares):

    costs = [[INF if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

    for c, d, f in fares:
        costs[c][d] = f
        costs[d][c] = f

    cost_s = dijkstra(costs, n, s)
    cost_a = dijkstra(costs, n, a)
    cost_b = dijkstra(costs, n, b)

    return min([cost_s[i] + cost_a[i] + cost_b[i] for i in range(1, n + 1)])
