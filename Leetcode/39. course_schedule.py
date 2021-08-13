# DFS
# 순환구조찾기 216 ms	33.1 MB 시간복잡도가 너무 구리다
# My answer
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
            
        def dfs(key, path):              
            # 순환이 아니므로 종료
            if len(graph[key]) == 0:
                return True
            
            next_keys = graph[key] # next_key는 여러가지 일수 있다
            for next_key in next_keys:
                if next_key in path:
                    return False
                
                if not dfs(next_key, path + [next_key]):
                    return False
                # 순환이 아니라고 판단되면 최적화를 위해 뒷단 삭제
                graph[key].remove(next_key)
            
            return True
        
        for key in list(graph):
            if not dfs(key, [key]):
                return False
            
        return True
