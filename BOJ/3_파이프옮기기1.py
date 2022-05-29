# 17070 파이프 옮기기1
# 삼성 A형 기출문제
# 백트래킹 or DP
# 아래 DFS 풀이는 시간초과임. 파이썬으로는 DP로 풀어야 통과됨

import sys
input = sys.stdin.readline
N = int(input().strip())
M = []
for i in range(N):
    M.append(list(map(int, input().strip().split())))

def move(left, right, type):
    x, y = left
    m, n = right
    
    # 가로
    if type == 0:
        return([[x, y+1], [x, y+1]], [[m, n+1], [m+1, n+1]])
    # 세로
    elif type == 1:
        return([[x+1, y], [x+1, y]], [[m+1, n], [m+1, n+1]])
    # 대각선
    else:
        return([[x+1, y+1], [x+1, y+1], [x+1, y+1]], [[m, n+1], [m+1, n], [m+1, n+1]])

count = 0
def dfs(left, right):
    global count
    
    if right == [N, N]:
        count += 1
        return
    
    if left[0] == right[0]:
        type = 0
    elif left[1] == right[1]:
        type = 1
    else:
        type = 2
        
    next_lefts, next_rights = move(left, right, type)
    for next_left, next_right in zip(next_lefts, next_rights):
        x, y = next_left
        m, n = next_right
        # 벗어난 경우
        if m > N or n > N:
            continue
        # right가 벽인 경우
        if M[m - 1][n - 1] == 1:
            continue
        # next 형태가 대각선인 경우
        if x != m and y != n:
            if M[x][y-1] == 1 or M[x-1][y] == 1:
                continue
        dfs(next_left, next_right)
    
left = [1, 1]
right = [1, 2]
if M[N-1][N-1] == 1:
    print(0)
else:
    dfs(left, right)
    print(count)
