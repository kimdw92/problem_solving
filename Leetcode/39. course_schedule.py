# DFS
# 순환구조찾기 
# My answer
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
            
        visited = set()
        def dfs(key, path):  
            if key in path:
                return False
            if key in visited:
                return True
            
            # next_key는 여러가지 일수 있다
            for next_key in graph[key]:              
                if not dfs(next_key, path + [key]):
                    return False
                # 순환이 아니라고 판단되면 최적화를 위해 뒷단 삭제
            
            visited.add(key)
            return True
        
        for key in list(graph):
            if not dfs(key, []):
                return False
            
        return True
    
    
# 다른 풀이
# path 대신에 set() 이용
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
            
        # 이미 방문한 곳
        traced = set()
        # 탐색이 끝난 후
        visited = set()
        
        
        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문한 노드이면 True
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
                
            # 탐색 종료 후 순환 노드 탐색
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
