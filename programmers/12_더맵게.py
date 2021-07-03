# 힙
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        now = heapq.heappop(scoville)
        if now >= K:
            return answer
            break
        if len(scoville) == 0:
            return -1
        next = heapq.heappop(scoville)
        new = now + (next * 2)
        heapq.heappush(scoville, new)
        answer += 1
        
    return -1
