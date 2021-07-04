# 그래프
# 최단경로
# 다익스트라 or BFS
import collections
import heapq
def solution(n, edge):
    answer = 0
    graph = collections.defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    Q = [(0, 1)]
    dist = collections.defaultdict(int)
    
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v in graph[node]:
                alt = time + 1
                heapq.heappush(Q, (alt, v))
    dists = sorted(list(dist.values()), reverse=True)
    prev = dists[0]
    for d in dists:
        if d < prev:
            break
        answer += 1
    return answer
