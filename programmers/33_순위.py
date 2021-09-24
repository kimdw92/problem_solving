# level 3
# 그래프
# 풀이를 생각해내기 어려운 문제
# 모든 상대와의 승패를 결정할수 있으면 순위를 알 수있다
# -> 플로이드-워셜로 구해진 거리 = 승패 여부

def solution(n, results):
    # 플로이드-워셜 알고리즘으로 거리 구하기
    # A가 B선수를 이기면 graph[A][B] < INF
    # 승패를 결정할수없으면 graph[A][B] = INF
    INF = 1e9
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    
    for winner, loser in results:
        graph[winner][loser] = 1
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
         
    # 다른 모든 선수와의 거리가 유한하면 (INF가 아니면) 순위를 매길수 있다
    answer = 0
    for a in range(1, n+1):
        cnt = 0
        for b in range(1, n+1):
            if graph[a][b] < INF or graph[b][a] < INF:
                cnt += 1
        if cnt == n:
            answer += 1
    return answer
