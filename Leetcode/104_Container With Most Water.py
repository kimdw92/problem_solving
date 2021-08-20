# 11. Container With Most Water
# Medium (체감은 easy)
# Two pointer

# My answer 752 ms	27.8 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            left_h, right_h = height[left], height[right]
            area = (right - left) * min(left_h, right_h)
            max_area = max(max_area, (right - left) * min(left_h, right_h))
            if left_h > right_h:
                right -= 1
            else:
                left += 1
        
        return max_area
