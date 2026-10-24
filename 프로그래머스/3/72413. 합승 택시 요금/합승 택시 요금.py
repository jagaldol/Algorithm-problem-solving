import heapq


def solution(n, s, a, b, fares):
    
    # s -> v + v -> a + v -> b
    
    adj = [[] for _ in range(n + 1)]
    
    for u, v, cost in fares:
        adj[u].append((v, cost))
        adj[v].append((u, cost))
    
    def dijkstra(start):
        costs = [float('inf')] * (n + 1)
        costs[start] = 0
        pq = [(0, start)]
        
        
        while pq:
            total_cost, city = heapq.heappop(pq)
            
            if total_cost > costs[city]:
                continue
            
            for neighbor, cost in adj[city]:
                new_cost = total_cost + cost
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
        
        return costs
    
    s_costs = dijkstra(s)
    a_costs = dijkstra(a)
    b_costs = dijkstra(b)
    
    return min(s_costs[i] + a_costs[i] + b_costs[i] for i in range(1, n + 1))
