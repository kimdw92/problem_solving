# 백준에도 있는 typical dp 문제
# level 3

def solution(triangle):
    dp = []
    for i, floor in enumerate(triangle):
        dp.append([0] * len(floor))
        if i == 0:
            dp[i][0] = triangle[i][0]
            continue
            
        for j, n in enumerate(floor):
            if j == 0:
                dp[i][j] = dp[i-1][j] + n
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + n
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + n
    return max(dp[-1])
