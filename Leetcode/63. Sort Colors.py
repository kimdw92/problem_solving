# 75 색정렬
# 유명한 네덜란드 국기 문제
# 퀵 정렬의 분할을 세 부분으로 개선한 방안을 제시한다
# 3개의 포인터를 이용해서 스왑해가며 푼다
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0 # red
        b = 0 # white
        c = len(nums) # blue
        
        while b < c:
            if nums[b] < 1:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1
            elif nums[b] > 1:
                c -= 1
                nums[c], nums[b] = nums[b], nums[c]
            else:
                b += 1
