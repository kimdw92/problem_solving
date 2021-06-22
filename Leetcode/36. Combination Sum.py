# 39 조합의 합
# DFS, 중복조합
 def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []        
        
        def dfs(cand, idx):
            if sum(cand) > target:
                return
            elif sum(cand) == target:
                result.append(cand[:])
                return
            for i in range(idx, len(candidates)):
                cand.append(candidates[i])
                dfs(cand, i)
                cand.pop()        
        
        dfs([], 0)
        return result
