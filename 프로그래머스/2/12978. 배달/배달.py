import heapq

def solution(N, road, K):
    answer = 0
    
    adj = [[] for _ in range(N + 1)]
    for u, v, cost in road:
        adj[u].append((v, cost))
        adj[v].append((u, cost))
    
    costs = [float('INF')] * (N + 1)
    
    pq = [(0, 1)]

    
    while pq:
        total_cost, city = heapq.heappop(pq)
        if total_cost > K:
            break
        costs[city] = total_cost
        
        for neighbor, cost in adj[city]:
            if costs[neighbor] > total_cost + cost:
                heapq.heappush(pq, (total_cost + cost, neighbor))
    
    return sum(1 for cost in costs if cost <= K)