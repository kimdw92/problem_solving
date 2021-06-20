# 200. 섬의 개수
# DFS로 그래프 탐색
# My answer
def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dx = [-1, 1, 0, 0] #서,동,북,남
        dy = [0, 0, -1, 1]
        result = 0
        m, n = len(grid), len(grid[0])
        
        def dfs(x: int, y: int):
            grid[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if grid[nx][ny] == '1':
                        dfs(nx, ny)
            return
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        return result
