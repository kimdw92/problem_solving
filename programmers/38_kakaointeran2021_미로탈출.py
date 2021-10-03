# level 4

# 다익스트라 변형 문제

# My answer: 테스트케이스 5, 7, 8, 18, 24 실패... (왜!??)
import heapq
import collections

def solution(n, start, end, roads, traps):
    # 다익스트라 최단경로 알고리즘
    graph = collections.defaultdict(list)
    # 마지막 1 or -1은 in or out을 나타내는 파라미터
    for p, q, s in roads:
        graph[p].append([q, s, 1])
        graph[q].append([p, s, -1])

    dist = collections.defaultdict(int)
    Q = [(0, start)]
    while Q:
        time, node = heapq.heappop(Q)
        # 해당 노드가 트랩이면 연결된 간선방향 바꿈
        if node in traps:
            for i in range(len(graph[node])):
                q, s, inout = graph[node][i]
                graph[node][i][-1] = -graph[node][i][-1]
                graph[q].remove([node, s, graph[node][i][-1]])
                graph[q].append([node, s, -graph[node][i][-1]])
                
        # 다익스트라 최단 거리 업데이트
        if node not in dist:
            if node == end: return time
            dist[node] = time
        # 다익스트라 힙큐 업데이트
        for n_node, n_time, inout in graph[node]:
            if inout < 0: continue
            alt = time + n_time
            heapq.heappush(Q, (alt, n_node))
