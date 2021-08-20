# 10. Regular Expression Matching
# Hard

# 재귀를 이용한 풀이 1352 ms	14.2 MB
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        
        # 첫 문자 일치 여부
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        # 패턴의 다음문자가 *이면
        if len(p) >= 2 and p[1] == '*':
            # 첫 문자가 일치 안하면 *를 이용해 패턴 첫글자 무시
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
                    # 첫문자가 일치하면 *를 계속 살려두면서 s의 다음 문자 비교
                    
        # 패턴의 다음 문자가 *가 아니면
        else:
            # 그냥 다음 문자 비교
            return first_match and self.isMatch(s[1:], p[1:])
        
# DP, 하향식 36 ms	14.6 MB
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p): # 패턴이 None이면
                    ans = (i == len(s)) # 텍스트도 None이어야 True
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        ans = first_match and dp(i+1, j+1)
                        
                memo[i, j] = ans
            return memo[i, j]
    
        return dp(0, 0)

# DP, 상향식
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        dp[-1][-1] = True
        
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
