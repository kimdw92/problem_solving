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
