# 167 두 수의 합 2

# My answer, 투 포인터, O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left+1, right+1]
              
# 이진 검색, O(nlogn)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1
            expect = target - v
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] < expect:
                    left = mid + 1
                elif numbers[mid] > expect:
                    right = mid - 1
                else:
                    return k+1, mid+1
                  
# 이진검색 모듈, (주의) 슬라이싱은 속도를 저하시킨다.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expect = target - v
            i = bisect.bisect_left(numbers, expect, k+1) # bisect.bisect_left(a, x, lo=0, hi=len(a))  에서 low index를 k+1로 지정
            if i < len(numbers) and numbers[i] == expect:
                return k + 1, i + 1
