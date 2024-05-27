import heapq

def solution(n, works):
    answer = 0
    pq = [-work for work in works]
    heapq.heapify(pq)
    for i in range(n):
        if len(pq) == 0:
            return 0
        current = heapq.heappop(pq)
        if current < 0:
            heapq.heappush(pq, current + 1)
    
    
    return sum([work**2 for work in pq])