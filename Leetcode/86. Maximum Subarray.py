# 53 최대 서브 배열
# DP

# 아이디어: 차례대로 더하는데, i번째 값부터 다시 더하는게 더 크면 리셋

# 풀이1 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_now = 0
        sum_best = -sys.maxsize
        for num in nums:
            sum_now = max(num, sum_now+num)
            sum_best = max(sum_best, sum_now)
        return sum_best
      
# 풀이2 메모이제이션
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        for idx, num in enumerate(nums):
            if idx == 0:
                sums.append(num)
                continue
            
            sums.append(num + sums[-1] if num + sums[-1] > num else num)
            
        return max(sums)

# 풀이2를 간단화 (공간복잡도 good)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nums)
