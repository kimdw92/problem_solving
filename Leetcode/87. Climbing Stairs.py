# 70 계단 오르기
# DP

# My answer, 메모이제이션
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = collections.defaultdict(int)
        for i in range(1, n+1):            
            if i <= 2:
                steps[i] = i
                continue
            
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]

# 메모이제이션2
class Solution:
    steps = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:    
        if n <= 2:
            return n
        
        if self.steps[n]:
            return self.steps[n]
        
        self.steps[n] = self.climbStairs(n-1) + self.climbStairs(n-2)        
        return self.steps[n]
        
