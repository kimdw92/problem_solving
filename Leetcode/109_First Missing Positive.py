# 41 First Missing Positive
# Hard
# Array, Hash table
# 제약조건: time O(n), space O(1)

# 풀이1 time O(n), space O(n)
# time complexity of 'in' -> list, tuple: O(n), set, dict: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i
            
            
# 풀이2 time O(n), space O(1)
"""
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [0] + nums
        for i in range(1,len(nums)):
            if nums[i] >= len(nums) or nums[i] <0:
                nums[i] = 0
        
        for i in range(1,len(nums)):
            target = nums[i] % len(nums)
            nums[target] += len(nums)
        
        for i in range(1,len(nums)):
            if nums[i] < len(nums):
                return i
        return len(nums)
