# 406 키에 따른 대기열 재구성

# 그리디 문제의 대부분은 우선순위 큐를 활용해 풀이한다. (여기서는 최대힙)
# 나는 sort(reverse=True)로 시도했지만, h는 내림차순, k는 오름차순이 필요하기 때문에 실패
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for h, k in people:
            heapq.heappush(heap, (-h, k))
        
        result = []
        while heap:
            h, k = heapq.heappop(heap)
            if len(result) == 0:
                result.append([-h, k])
                continue
            # 높은 인덱스부터 뽑아냈기 때문에 그 인덱스에 그대로 삽입하면 된다.
            result.insert(k, [-h, k])
            
        return result
