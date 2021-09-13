# 모르면 막막한 문제

# 최단 경로 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 할 때는
# Floyd-Warshall Algorithm
def solution(n, s, a, b, fares):
    INF = 1e9
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    # 자기 자신에서 자기 자신으로 가는 비용은 0
    for _a in range(1, n+1):
        for _b in range(1, n+1):
            if _a ==_b:
                graph[_a][_b] = 0
        
    # 각 간선에 대한 정보로 초기화
    for fare in fares:
        n1, n2, f = fare
        graph[n1][n2] = f
        graph[n2][n1] = f
        
    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n+1):
        for _a in range(1, n+1):
            for _b in range(1, n+1):
                graph[_a][_b] = min(graph[_a][_b], graph[_a][k] + graph[k][_b])

    # 출발지점 s  -> 헤어지는 지점 x -> 각자의 집 a,b 
    # 합 요금이 최소가 되는 경우를 완전탐색
    answer = 1e9
    for x in range(1, n+1):
        s_to_x = graph[s][x]
        x_to_a = graph[x][a]
        x_to_b = graph[x][b]
        answer = min(answer, s_to_x + x_to_a + x_to_b)        
    
    return answer
