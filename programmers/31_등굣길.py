# level 3
# dp

def solution(m, n, puddles):
    # m,n의 최단 경로 개수 = m-1,n 개수 + m, n-1 개수
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif [i, j] in puddles:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[m][n] % 1000000007
