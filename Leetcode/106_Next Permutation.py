# 31 Next Permutation
# Medium
# 투포인터, 조금 트리키한 문제... 솔루션을 봐야함
# 구현했는데 아직 안돌아감
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = len(nums)-2, len(nums)-1
        while left >= 0 and nums[left] >= nums[right]:
            if left == 0:
                break
            left -= 1
            right -= 1
          
        while right < len(nums) and nums[left] < nums[right]:
            right += 1    
            
        right -= 1
        print(left, right)
        if nums[left] < nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            print(nums)
            nums = nums[:left+1] + sorted(nums[left+1:])
            print(nums)
        else:
            nums.sort()
            
        print(nums)
            
            
            
