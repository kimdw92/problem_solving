# 743. 네트워크 딜레이 타임
# 최단 경로 문제
# 다익스트라 알고리즘 구현 O((V+E)logV), 모든 정점이 도달 가능하면 O(ElogV)
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐 변수: [(소요시간, 정점)]
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        
        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                    
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1
