# 62 Unique Paths
# Medium

# My answer
# DFS -> 시간 초과
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dx = [0, 1]
        dy = [1, 0]      
        x, y = 0, 0
        goal_x, goal_y = m-1, n-1
        cnt = 0
        def dfs(x, y):            
            if x >= m or y >= n:
                return
            if x == goal_x and y == goal_y:
                nonlocal cnt
                cnt += 1
                return           
            for i in range(2):
                dfs(x + dx[i], y + dy[i])  
        
        dfs(x, y)
        return cnt
      
# My answer2
# DP
# Runtime: 36 ms, faster than 25.91% of Python3 online submissions for Unique Paths.
# Memory Usage: 14.4 MB, less than 15.71% of Python3 online submissions for Unique Paths.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for x in range(1, m):
            for y in range(1, n):
                dp[x][y] = dp[x][y-1] + dp[x-1][y]
        
        return dp[m-1][n-1]
