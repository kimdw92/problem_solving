# 34 Find First and Last Position of Element in Sorted Array
# Medium
# Binary search / Two pointer

# My answer 80 ms	15.3 MB
# 이진 탐색 후 재탐색
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # binary search로 target 탐색
        left, right = 0, len(nums)-1
        index = []
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1
            else:
                index.append(mid)
                break
                
        # target이 없으면 종료
        if len(index) == 0:
            return [-1, -1]
        
        # 찾은 index를 중심으로 모든 target의 index 탐색
        left, right = mid - 1, mid + 1
        while True:
            if left >= 0 and nums[left] == target:
                index.append(left)
                left -= 1  
            elif right < len(nums) and nums[right] == target:
                index.append(right)
                right += 1
            else:
                break
        
        index.sort()
        return [index[0], index[-1]]
        
# 모범 답안 76 ms	15.4 MB
# target중 가장 왼쪽, 가장 오른쪽을 바로 찾을수 있음
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        # find left target
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if left < len(nums) and nums[left] == target:
            start = left
            
        # find right target
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
                
        if right-1 >= 0 and nums[right-1] == target:
            end = right-1
            
        return [start, end]
