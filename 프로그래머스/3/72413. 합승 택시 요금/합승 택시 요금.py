def solution(n, s, a, b, fares):
    
    # s -> v + v -> a + v -> b
    
    costs = [[float("INF")] * (n + 1) for _ in range(n + 1)]
    
    for u, v, cost in fares:
        costs[u][v] = cost
        costs[v][u] = cost
    
    for k in range(1, n + 1):
        costs[k][k] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
    
    
    return min(costs[s][v] + costs[v][a] + costs[v][b] for v in range(1, n + 1))
