# 215 배열의 K번째 큰 요소

# 풀이1: 정렬을 이용한 풀이
# sorted vs sort : sorted는 새로운 리스트를 반환하고, sort는 그 리스트를 바꾼다
def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
  
def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
