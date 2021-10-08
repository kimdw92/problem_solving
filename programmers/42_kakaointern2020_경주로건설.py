# level 3
# 백트래킹

# My answer, dfs, 시간초과
min_cost = 1e9
def solution(board):
    n = len(board)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    def dfs(x, y, prev, cost, visited):
        global min_cost
        if cost >= min_cost:
            return
        if x == n-1 and y == n-1:
            min_cost = cost
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if n > nx >= 0 and n > ny >= 0 and board[nx][ny] == 1:
                continue
            if n > nx >= 0 and n > ny >= 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if prev == 'start':
                    cost += 100
                else:
                    if prev == i:
                        cost += 100
                    else:
                        cost += 600
                dfs(nx, ny, i, cost, visited)
                visited[nx][ny] = 0
                if prev == 'start':
                    cost -= 100
                else:
                    if prev == i:
                        cost -= 100
                    else:
                        cost -= 600
                
    visited = [[0] * n for _ in range(n)]
    dfs(0, 0, 'start', 0, visited)
    return min_cost
