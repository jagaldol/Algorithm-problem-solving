import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    count = 0
    while scoville[0] < K and len(scoville) > 1:
        count += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
    
    return count if scoville[0] >= K else -1
