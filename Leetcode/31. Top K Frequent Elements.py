# 347. 상위 K 빈도 요소

# 풀이1: Counter와 우선수위큐(heapq)를 이용
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
            
        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
            
        return topk
      
# 풀이2: 파이썬다운 방식, zip(), 아스테리스크(*), Counter.most_common
# zip의 패러미터로 하나의 리스트가 들어갈때, 아스테리스트를 사용해서 언팩킹 해야 zip이 제대로 작동한다
# collections.Counter(nums).most_common(k) -> [(1, 3), (2, 2)]
# zip(*collections.Counter(nums).most_common(k)) -> [(1, 2), (3, 2)]
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
