# 179 가장 큰 수
# 삽입 정렬로 구현
class Solution:
    def to_swap(self, n1, n2):
        return str(n1) + str(n2) < str(n2) + str(n1)
                                                 
    def largestNumber(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str, nums))))
