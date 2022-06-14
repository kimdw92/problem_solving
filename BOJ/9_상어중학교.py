# 21609 상어중학교 골드2
# 구현 + BFS
# 애니팡
# 매트릭스 회전
# 중력 이동

from collections import deque
N, M = map(int, input().split())
MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().split())))
normal_blocks = [i for i in range(1, M+1)]
dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1]

def valid_pos(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True

def get_group(x, y):
    group = []
    color = MAP[x][y]
    num_rainbow = 0
    color_block = [(x, y)]
    q = deque()
    q.append((x, y))
    group.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not valid_pos(nx, ny) or visited[nx][ny] == 1 or MAP[nx][ny] < 0:
                continue
            if MAP[nx][ny] == color:
                visited[nx][ny] = 1
                q.append((nx, ny))
                color_block.append((nx, ny))
                group.append((nx, ny))
            elif MAP[nx][ny] == 0:
                if (nx, ny) in group:
                    continue
                num_rainbow += 1
                q.append((nx, ny))
                group.append((nx, ny))
    color_block.sort()
    # return 블록의 크기, 무지개블록의 수, 기준 블록, 그룹
    return len(group), num_rainbow, (color_block[0][0], color_block[0][1]), group

def activate_gravity():
    for j in range(N):
        for i in range(N-1,-1,-1):
            if MAP[i][j] >= 0:
                x, y = i, j
                while x >= 0 and x+1<N and MAP[x+1][y] == -2:
                    MAP[x+1][y], MAP[x][y] = MAP[x][y], MAP[x+1][y]
                    x += 1
score = 0
while True:
    # 모든 그룹 찾기
    # 일반블록 1개 이상
    # 검은블록 x
    # 블록개수 2개 이상
    # 기준블록
    # 블록길이가 가장 큰
    groups = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and MAP[i][j] > 0:
                visited[i][j] = 1
                group_size, rainbow_size, standard, group = get_group(i, j)
                if group_size >= 2:
                    groups.append([group_size, rainbow_size, standard, group])
    if len(groups) == 0:
        break
    groups.sort(reverse=True)


    # 블록 제거
    score += len(groups[0][3]) ** 2
    for x, y in groups[0][3]:
        if MAP[x][y] < 0:
            print('something is wrong')
        MAP[x][y] = -2
    # 중력 적용
    activate_gravity()
    # 90도 반시계 회전
    rotated_MAP = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_MAP[N-j-1][i] = MAP[i][j]
    MAP = rotated_MAP
    # 중력 적용
    activate_gravity()

print(score)
