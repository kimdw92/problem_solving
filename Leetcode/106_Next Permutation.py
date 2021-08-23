# 31 Next Permutation
# Medium
# 투포인터, 조금 트리키한 문제... 솔루션을 봐야함
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return nums
        
        left, right = len(nums)-2, len(nums)-1
        while nums[left] >= nums[right]:
            if left == 0:
                break
            left -= 1
            right -= 1
          
        while right < len(nums) and nums[left] < nums[right]:
            right += 1                
        right -= 1
        
        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            nums[left+1:] = sorted(nums[left+1:])
        else:
            nums.sort()
            
            
            
