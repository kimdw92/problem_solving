# 55 Jump Game
# Medium

# My answer
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        left, right = 0, nums[0]
        
        while right < len(nums)-1:
            nxt = max(i + nums[i] for i in range(left, right+1))
            left, right = right, nxt
            if left == right:
                return False
        return True
