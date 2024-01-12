import sys

INF = 1_000_000_000


def sol():
    N, M = map(int, input().split())

    buses = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        buses.append((A, B, C))

    dist = [INF if i != 1 else 0 for i in range(N + 1)]

    for i in range(N - 1):
        for A, B, C in buses:
            if dist[A] != INF and dist[B] > dist[A] + C:
                dist[B] = dist[A] + C

    for A, B, C in buses:
        if dist[A] != INF and dist[B] > dist[A] + C:
            print(-1)
            return

    for i in range(2, N + 1):
        print(dist[i] if dist[i] != INF else -1)


sol()
