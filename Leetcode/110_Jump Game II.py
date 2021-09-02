# 45 Jump Game 2
# Medium

# My answer
# DP
# Time Limit Exceeded... T.T
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = 0
        
        for i in range(1, len(nums)):
            dp = dict(sorted(dp.items(), key=lambda item: item[1]))
            for k, v in dp.items():
                if nums[k] >= i-k:
                    dp[i] = v + 1
                    break
    
        return dp[len(nums)-1]
            
# My answer 2 2350 ms	15.3 MB
# greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        steps = 0
        right = len(nums) - 1
        left = 0
        while right > 0:
            if nums[left] >= right - left:
                steps += 1
                left, right = 0, left
            else:
                left += 1
                
        return steps
      
      
# More fast solution
# greedy
def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times
