# 64 Minimum Path Sum
# Medium

# My answer
# DP
import sys
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
                    dp[x][y] = grid[x][y]
                    continue
                left = dp[x][y-1] if y > 0 else sys.maxsize
                up = dp[x-1][y] if x > 0 else sys.maxsize
                dp[x][y] = min(left, up) + grid[x][y]
        return dp[-1][-1]
