def solution(n, s, a, b, fares):
    INF = 1_000_000_000

    costs = [[INF if i != j else 0 for j in range(201)] for i in range(201)]

    for c, d, f in fares:
        costs[c][d] = f
        costs[d][c] = f

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                costs[j][k] = min(costs[j][i] + costs[i][k], costs[j][k])

    return min([costs[s][k] + costs[k][a] + costs[k][b] for k in range(k + 1)])
