# 973 원점에서 K번째로 가까운 점
# my answer, 최소 힙
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, [dist, [x, y]])
            
        answer = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            answer.append(point)
            
        return answer
