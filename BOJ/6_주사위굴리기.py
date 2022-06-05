# 23288 주사위굴리기2
# 삼성 SW역량 기출문제
# 시뮬레이션 + 그래프탐색

from collections import deque

N, M, K = map(int, input().split())
D = []
for _ in range(N):
  D.append(list(map(int, input().split())))

# 0:동 1:북 2:서 3:남
way = 0
dice = [2, 1, 5, 6, 4, 3]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def next_dice(way):
  if way == 0:
    dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
  elif way == 1:
    dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
  elif way == 2:
    dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]
  else:
    dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]

def next_way(way, right = True):
  if right == True:
    way -= 1
    return way if way >= 0 else 3
  else:
    way += 1
    return way if way <= 3 else 0
    
score = 0
x, y = [0, 0]
for i in range(K):
  nx, ny = x + dx[way], y + dy[way]
  # 주사위가 맵에서 벗어날 경우 반대 방향으로
  if nx >= N or nx < 0 or ny >= M or ny < 0:
    way = next_way(next_way(way))
    next_dice(way)
    nx, ny = x + dx[way], y + dy[way]
  else:
    next_dice(way)
    
  # 점수 계산
  B = D[nx][ny]
  C = 0
  q = deque()
  q.append((nx, ny))
  visited = [[0] * M for _ in range(N)]
  visited[nx][ny] = 1
  while q:
    x, y = q.popleft()
    C += 1
    for i in range(4):
      _x, _y = x + dx[i], y + dy[i]
      if _x >= N or _x < 0 or _y >= M or _y < 0:
          continue
      if D[_x][_y] == B and visited[_x][_y] == 0:
        q.append((_x, _y))
        visited[_x][_y] = 1
  
  score += C * B
  x, y = nx, ny

  A = dice[3]
  if A > B:
    way = next_way(way)
  elif A < B:
    way = next_way(way, False)

print(score)
