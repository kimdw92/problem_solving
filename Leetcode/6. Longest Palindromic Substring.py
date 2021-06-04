# 06 가장 긴 팰린드롬 부분 문자열
# DP로도 풀수 있지만, 여기서는 투포인터가 빠름
# while 종료 이전 값으로 뽑아야하는거 주의!
# max(a,b,c, key = len) : 길이로 max 리턴

# My answer 단순 완전반복, 6592 ms	14.2 MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = s[0]
        for i in range(len(s)):
            if i >= (len(s) - len(output)):
                break
            for j in range(i+len(output), len(s)):
                temp = s[i:j+1] 
                if temp == temp[::-1]:
                    if len(temp) > len(output):
                        output = temp
        return output
    
    
# 풀이1 중앙을 중심으로 확장하는 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 투포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right] # while 종료 이전 값으로 뽑아야하는거 주의!
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우 우측 이동
        for i in range(len(s) - 1):
            result = max(result,
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key = len)
        return result
