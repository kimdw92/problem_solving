# 22 Generate Paranthese
# Medium
# Backtracking

# My answer
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        do = {'(' : 1, ')' : -1}
        result = []
        def dfs(pars, num):
            if len(pars) == n*2 and num == 0:
                result.append(pars)
                return
            elif len(pars) == n*2 and num > 0:
                return
            elif num < 0 or num > n:
                return
            
            for add in ['(', ')']:
                dfs(pars + add, num + do[add])
                
        dfs('', 0)
        return result
