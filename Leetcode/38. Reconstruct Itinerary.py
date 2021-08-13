# 332 일정 재구성 

# My answer
# 그다지 깔끔하지 못한 dfs 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        def dfs(path, idxs):
            # 여정을 끝냈다면 탐색 종료
            if len(path) == len(tickets) + 1:
                answer.append(path)
                return
            
            # 첫 번째 찾은 답이 정답이므로 그 이후는 탐색 x
            if len(answer) > 0:
                return
            
            # 안가본 여정 중, 이전 도착지가 출발지가 되는 여정들의 후보지 탐색
            candi = []
            for idx, [fromi, toi] in enumerate(tickets):
                if fromi == path[-1] and idx not in idxs:
                    candi.append([fromi + toi, idx])
            
            # 다음 여정을 찾을수 없다면 탐색 종료
            if len(candi) == 0:
                return
            
            # lexcial order으로 다음 여정지 고르기
            candi.sort()
            for fromto, idx in candi:
                dfs(path + [fromto[3:]], idxs + [idx])
        
        dfs(['JFK'], [])
        return answer[0]
      
# 정석 풀이
# dict 구성
# JFK -> NRT -> JFK -> KUL : 중간에 끊기는 경우,,,?? 이해가 잘 안됨
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route = []
        def dfs(a):      
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)      #????   
        
        dfs('JFK')
        return route[::-1]
    
# 반복으로 풀이
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
            
        return route[::-1]
