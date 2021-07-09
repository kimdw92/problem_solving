# 455 쿠키 부여, easy
# 그리디
# My answer
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        g.sort()
        s.sort(reverse=True)
        for want in g:
            if len(s) == 0:
                return answer
            while s:
                cookie = s.pop()
                if cookie >= want:
                    answer += 1
                    break
                                
        return answer

# 다른 풀이
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child_i = cookie_j = 0
        
        while child_i < len(g) and cookie_j < len(s):
            if g[child_i] <= s[cookie_j]:
                child_i += 1
            cookie_j += 1
            
        return child_i
