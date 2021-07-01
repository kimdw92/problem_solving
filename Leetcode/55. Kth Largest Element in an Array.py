# 215 배열의 K번째 큰 요소

# 풀이1: 정렬을 이용한 풀이
# sorted vs sort : sorted는 새로운 리스트를 반환하고, sort는 그 리스트를 바꾼다
def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
  
def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


# 풀이2: heapq 모듈 이용
def findKthLargest(self, nums: List[int], k: int) -> int:
        q = list()
        for num in nums:
            heapq.heappush(q, -num)
            
        
        for _ in range(1, k):
            heapq.heappop(q)
        return -heapq.heappop(q)

# 풀이3: heapify()는 리스트를 힙 특성을 만족하는 리스트로 바꾼다
def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
            
        return heapq.heappop(nums)

# 풀이4: heapq.nlargest(k, nums)[-1] 힙 아닌 리스트를 힙으로 바꿔서 k번재 큰 값을 리턴 / 참고로 nsmallest()도 있음
def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
