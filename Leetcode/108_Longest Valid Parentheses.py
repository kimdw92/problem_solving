# 32 Longest Valid Parentheses
# Hard

# DP문제인데 DP로 푸는건 좀 난해하고
# leetcode solution4 참고 (투포인터) https://leetcode.com/problems/longest-valid-parentheses/solution/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid, length = 0, 0
        longest = 0
        # traverse left to right
        for char in s:
            if char == '(': valid += 1
            elif char == ')': valid -= 1
            length += 1
            
            # if ')' is more than '(', reset count
            if valid < 0:
                valid = 0
                length = 0
                continue
            
            # if valid parentheses, update longest
            if valid == 0:
                longest = max(longest, length)
                      
        valid, length = 0, 0
        # traverse right to left
        for char in s[::-1]:
            if char == ')': valid += 1
            elif char == '(': valid -= 1
            length += 1
            
            # if '(' is more than ')', reset count
            if valid < 0:
                valid = 0
                length = 0
                continue
            
            # if valid parentheses, update longest
            if valid == 0:
                longest = max(longest, length)
 
        return longest
            
            
            
                
            
