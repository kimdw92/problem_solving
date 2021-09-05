# 79 Word Search
# Medium

# My asnwer
# DFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        answer = False
        
        def dfs(x, y, cnt, visited):
            if cnt == len(word)-1:
                nonlocal answer
                answer = True
                return            
          
            for direction in range(4):
                nx, ny = x + dx[direction], y + dy[direction]
                if nx >= 0 and ny >= 0 and nx < m and ny < n and board[nx][ny] == word[cnt+1] and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx, ny, cnt+1, visited)
                    visited[nx][ny] = 0
    
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[0] * n for _ in range(m)]
                    visited[i][j] = 1
                    if dfs(i, j, 0, visited):
                        return True
        
        return answer
