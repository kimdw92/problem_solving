# dfs
# LEECODE 섬개수 구하는 문제랑 똑같음
answer = 0
def solution(n, computers):
    global answer
    
    visited = [0] * n
    def dfs(node):        
        for next_node in range(n):
            if visited[next_node] == 0:
                if computers[node][next_node] == 1:
                    visited[next_node] = 1
                    dfs(next_node)
        return
        
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            answer += 1
        
    return answer
