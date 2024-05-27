import heapq

def solution(n, works):
    heapq.heapify(pq := [-work for work in works])
    
    for i in range(n):
        if len(pq) == 0:
            return 0
        if (current := heapq.heappop(pq)) < 0:
            heapq.heappush(pq, current + 1)
    
    return sum([work**2 for work in pq])