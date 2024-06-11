import sys, heapq

INF = 1_000_000_000


def sol():
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    cost_map = [[] for _ in range(N + 1)]

    for i in range(M):
        s, e, cost = map(int, input().split())
        cost_map[s].append((e, cost))

    s, e = map(int, input().split())

    dist = [INF for _ in range(N + 1)]

    pq = []
    heapq.heappush(pq, (0, s))

    dist[s] = 0

    while len(pq) > 0:
        now_cost, city = heapq.heappop(pq)
        if city == e:
            break

        for dest, cost in cost_map[city]:
            total = now_cost + cost
            if total < dist[dest]:
                dist[dest] = total
                heapq.heappush(pq, (total, dest))

    print(dist[e])


sol()
