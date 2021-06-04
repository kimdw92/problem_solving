# My answer 196 ms	18.7 MB  (한 줄로 푸는 Pythonic way)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()
        

# 투 포인터를 이용한 스왑 200 ms	18.6 MB
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
