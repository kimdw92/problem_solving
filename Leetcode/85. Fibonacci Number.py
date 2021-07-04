# 다이나믹 프로그래밍
# 509 피보나치 넘버

# 메모이제이션(하향식)
class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]
      
# 타뷸레이션(상향식)      
class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, n: int) -> int:
        self.dp[1] = 1
        
        for i in range(2, n+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[n]
