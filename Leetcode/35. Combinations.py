# 77. 조합

# DFS
def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
           
        def dfs(idx, count, comb):
            if count >= k:
                result.append(comb[:])
                return
            for i in range(idx, n+1):
                comb.append(i)
                dfs(i+1, count+1, comb)
                comb.pop()
                   
        dfs(1, 0, [])
        return result
      
# itertools 모듈 사용      
def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1,n+1), k))
