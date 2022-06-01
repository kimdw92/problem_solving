# 17472 다리만들기2
# 삼성A형 기출문제
# 완전탐색 + 그래프탐색 + 최소신장트리(크루스칼)
# 크루스칼 알고리즘 구현방법을 미리 외워놔야 풀수있음

import itertools

N, M = map(int, input().split())
D = []
for _ in range(N):
    D.append(list(map(int, input().split())))

# 섬 찾기 -> DFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, island):
    island.append([x, y])
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if D[nx][ny] == 0 or visited[nx][ny] == 1:
            continue
        visited[nx][ny] = 1
        dfs(nx, ny, island)
    return island

islands = []
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and D[i][j] == 1:
            visited[i][j] = 1
            island = dfs(i, j, [])
            islands.append(island)

n_island = len(islands)

# 다리 만들기 -> 완전 탐색
combis = list(itertools.combinations(range(n_island), 2))
dist = [-1] * len(combis)
for idx, [left, right] in enumerate(combis):
    distance = 1e9
    for x_left, y_left in islands[left]:
        for way in range(4):
            nx, ny = x_left, y_left
            length = 0
            while True:
                if length >= 2 and [nx + dx[way], ny + dy[way]] in islands[right]:
                    distance = min(distance, length)
                nx += dx[way]
                ny += dy[way]
                length += 1
                if nx>= N or nx < 0 or ny>= M or ny< 0 or D[nx][ny] == 1:
                    break

    if distance < 1e9:
        dist[idx] = distance
#print(combis)
#print(dist)
#[(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
#[-1, -1, 4, 4, -1, 2]
# 다리 길이의 최솟값 구하기 -> 최소신장트리 크루스칼 알고리즘
edges = []
for i in range(len(dist)):
    if dist[i] >= 2:
        edges.append((dist[i], *combis[i]))
        
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수 = n_island
# 간선의 개수 = len(edges)

# 부모 테이블을 자기 자신으로 초기화
parent = [i for i in range(n_island)]

result = 0

edges.sort() # 간선을 비용 순으로 정렬

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 연결 안된 섬이 있는지 체크(parent의 수가 1이어야 함)
n_parent = 0
for node in range(n_island):
    if find_parent(parent, node) == node:
        n_parent += 1

if n_parent > 1 or result == 0:
    print(-1)
else:
    print(result)

