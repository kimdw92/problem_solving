# level 4
# dp

# 조금 헤맬 수 있는 문제
# 두가지 경우의 수
def solution(money):
    # dp[n] = max(dp[n-1], dp[n-2] + money[n])
    dp = [0] * len(money)
    dp2 = [0] * len(money)
    
    # 첫번째 집을 턴 경우
    dp[0] = money[0]
    dp[1] = money[0]
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    
    # 첫번째 집을 안턴 경우
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    return max(dp[-2], dp2[-1])
