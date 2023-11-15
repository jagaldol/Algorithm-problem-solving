import sys


def sol():
    input = sys.stdin.readline

    INF = 1000000000

    n = int(input())
    m = int(input())

    cost = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(m):
        a, b, c = map(int, input().split())
        cost[a][b] = min(c, cost[a][b])

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(cost[i][j] if cost[i][j] != INF else 0, end=" ")
        print()


sol()
