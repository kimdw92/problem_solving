# 198 집도둑
# DP

# My answer 타뷸레이션
# i번째 집 까지 털 수 있는 최대 금액 = max(i-1번째 집 까지 최대 금액, i-1번째 까지 최대 금액 + i번째 돈)
class Solution:
    dp = collections.defaultdict(int)
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return max(nums)
        
        self.dp[1] = nums[0]
        self.dp[2] = max(nums[0], nums[1])
        
        for i in range(3, l+1):
            self.dp[i] = max(self.dp[i-1], self.dp[i-2] + nums[i-1])
            
        return self.dp[l]
