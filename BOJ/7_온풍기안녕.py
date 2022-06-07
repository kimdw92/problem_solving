# 23289 온풍기 안녕!
# 삼성 sw역량 기출
# 빡센 시뮬레이션 구현

R, C, K = map(int, input().split())
D = []
heater = [] # 온풍기 위치
invest = [] # 온도를 조사하는 칸의 위치
for i in range(R):
    D.append(list(map(int, input().split())))
    for j in range(C):
        if D[i][j] == 5:
            invest.append((i, j))
        elif D[i][j] == 0:
            continue
        else:
            heater.append((i, j, D[i][j]))

W = int(input())
RIGHT_W = [[0] * C for _ in range(R)]
UP_W = [[0] * C for _ in range(R)]
for _ in range(W):
    xw, yw, ww = map(int, input().split())
    if ww == 1:
        RIGHT_W[xw-1][yw-1] = 1
    elif ww == 0:
        UP_W[xw-1][yw-1] = 1

# 온도 맵
T = [[0] * C for _ in range(R)]
# 집에 있는 모든 온풍기에서 바람이 한 번 나옴
# 온도가 조절됨
# 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
# 초콜릿을 하나 먹는다.
# 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.

# 사이에 벽이 있는지 판단
def check_wall(x, y, nx, ny):
    if x == nx:
        if y > ny and RIGHT_W[nx][ny] == 1:
            return True
        elif y < ny and RIGHT_W[x][y] == 1:
            return True
    elif y == ny:
        if x > nx and UP_W[x][y] == 1:
            return True
        elif x < nx and UP_W[nx][ny] == 1:
            return True
    return False

# 위치가 유효한지 판단
def valid_pos(x, y):
    if x >= R or x < 0 or y >= C or y < 0:
        return False
    else:
        return True

# 온풍기 바람이 가는 다음 위치
def next_pos(x, y, way):
    pos = []
    if way == 1:
        if valid_pos(x-1, y+1) and RIGHT_W[x-1][y] != 1 and UP_W[x][y] != 1 : pos.append((x-1, y+1))
        if valid_pos(x, y+1) and RIGHT_W[x][y] != 1 : pos.append((x, y+1))
        if valid_pos(x+1, y+1) and RIGHT_W[x+1][y] != 1 and UP_W[x+1][y] != 1 : pos.append((x+1, y+1))
    elif way == 2:
        if valid_pos(x-1, y-1) and RIGHT_W[x-1][y-1] != 1 and UP_W[x][y] != 1 : pos.append((x - 1, y - 1))
        if valid_pos(x, y-1) and RIGHT_W[x][y-1] != 1 : pos.append((x, y - 1))
        if valid_pos(x+1, y-1) and RIGHT_W[x+1][y-1] != 1 and UP_W[x+1][y] != 1 : pos.append((x + 1, y - 1))
    elif way == 3:
        if valid_pos(x-1, y-1) and RIGHT_W[x][y-1] != 1 and UP_W[x][y-1] != 1 : pos.append((x - 1, y - 1))
        if valid_pos(x-1, y) and UP_W[x][y] != 1 : pos.append((x - 1, y))
        if valid_pos(x-1, y+1) and RIGHT_W[x][y] != 1 and UP_W[x][y+1] != 1 : pos.append((x - 1, y + 1))
    elif way == 4:
        if valid_pos(x+1, y-1) and RIGHT_W[x][y-1] != 1 and UP_W[x+1][y-1] != 1 : pos.append((x + 1, y - 1))
        if valid_pos(x+1, y) and UP_W[x+1][y] != 1 : pos.append((x + 1, y))
        if valid_pos(x+1, y+1) and RIGHT_W[x][y] != 1 and UP_W[x+1][y+1] != 1 : pos.append((x + 1, y + 1))
    return pos

# 재귀로 온풍기 바람 끝까지 보내기
def dfs(x, y, way, temp):
    if temp == 0:
        return
    T[x][y] += temp
    visited[x][y] = 1
    pos = next_pos(x, y, way)
    if len(pos) == 0:
        return
    for m, n in pos:
        if visited[m][n] == 0:
            dfs(m, n, way, temp-1)

choco = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 루프 시작
while True:
    # 2 온풍기에서 바람이 한 번 나옴
    for x, y, way in heater:
        visited = [[0] * C for _ in range(R)]
        if way == 1: # 오른쪽
            dfs(x, y+1, way, 5)
        elif way == 2: # 왼쪽
            dfs(x, y-1, way, 5)
        elif way == 3: # 위
            dfs(x-1, y, way, 5)
        else: # 아래
            dfs(x+1, y, way, 5)

    # 3 온도가 조절됨
    diff_matrix = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if not valid_pos(ni, nj) or check_wall(i, j, ni, nj):
                    continue
                if T[i][j] > T[ni][nj]:
                    diff = (T[i][j] - T[ni][nj]) // 4
                    diff_matrix[i][j] -= diff
                    diff_matrix[ni][nj] += diff
    for i in range(R):
        for j in range(C):
            T[i][j] += diff_matrix[i][j]

    # 4 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    for i in [0, R-1]:
        for j in range(C):
            T[i][j] -= 1
            if T[i][j] < 0:
                T[i][j] = 0
    for j in [0, C-1]:
        for i in range(1, R-1):
            T[i][j] -= 1
            if T[i][j] < 0:
                T[i][j] = 0

    # 5 초콜릿을 먹는다
    choco += 1
    if choco > 100:
        break

    # 1 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사
    flag = 0
    for x, y in invest:
        if T[x][y] >= K:
            flag += 1
    if flag == len(invest):
        break

print(choco)
