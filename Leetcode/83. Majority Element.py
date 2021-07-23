# 169 과반수 엘리먼트
# 분할정복

# My answer
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(int)
        n = len(nums)
        for num in nums:
            cnt[num] += 1
            if cnt[num] > n/2:
                return num

# DP(메모이제이션)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(int)
        for num in nums:
            if cnt[num] == 0:
                cnt[num] = nums.count(num)
                
            if cnt[num] > len(nums) // 2:
                return num
              
# 분할정복
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 값 리턴
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        
        # 분할
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        
        # 정복
        return [b, a][nums.count(a) > half]
      
# 파이썬다운방식
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
