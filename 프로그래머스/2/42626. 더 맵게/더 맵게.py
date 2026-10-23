import heapq

def solution(scoville, K):
    scoville = scoville.copy()
    heapq.heapify(scoville)
    
    count = 0
    while len(scoville) > 1 and scoville[0] < K:
        count += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
    
    return count if scoville[0] >= K else -1
