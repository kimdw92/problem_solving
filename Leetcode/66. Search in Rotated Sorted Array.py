# 33 회전 정렬된 배열 검색
# 피벗을 기준으로 한 이진 검색
def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        
        left, right = 0, len(nums)-1
        
        while left<=right:
            mid = left + (right-left)//2
            mid_pivot = (mid + pivot)%len(nums)
            
            if nums[mid_pivot] > target:
                right = mid - 1
            elif nums[mid_pivot] < target:
                left = mid + 1
            else:
                return mid_pivot
            
        return -1
