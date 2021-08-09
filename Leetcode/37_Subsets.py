# 78. 부분 집합
# 트리의 모든 dfs 결과
# My answer
# append와 pop을 쓰는 대신에 + [nums[i]] 이 더 간결함    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(idx, subset):
            result.append(subset)
            
            for i in range(idx, len(nums)):
                dfs(i+1, subset + [nums[i]])
                   
        dfs(0, [])
        return result
