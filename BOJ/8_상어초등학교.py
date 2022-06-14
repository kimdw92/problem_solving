# 21608 상어초등학교
# 골드5
# 단순 구현
N = int(input())
D = []
for _ in range(N*N):
    D.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

C = [[0] * N for _ in range(N)]

for i in range(N*N):

    num, like1, like2, like3, like4 = D[i]
    likes = [like1, like2, like3, like4]
    # 좋아하는 학생이 가장 많이 인접한 칸
    most_like = []
    candidates_1 = []
    for x in range(N):
        for y in range(N):
            if C[x][y] > 0: # 비어있는 칸 중에서
                continue
            temp = 0
            for way in range(4):
                nx, ny = x+dx[way], y+dy[way]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if C[nx][ny] in likes:
                    temp += 1
            most_like.append([temp, x, y])
    most_like.sort(reverse=True)
    like_this = most_like[0][0]
    for like, x, y in most_like:
        if like < like_this:
            break
        candidates_1.append([x, y])

    # 인접한 칸 중에서 빈칸이 많은 자리
    most_blank = []
    candidates_2 = []
    for x, y in candidates_1:
        temp = 0
        for way in range(4):
            nx, ny = x+dx[way], y+dy[way]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if C[nx][ny] == 0:
                temp += 1
        most_blank.append([temp, x, y])
    most_blank.sort(reverse=True)
    blank_this = most_blank[0][0]
    for blank, x, y in most_blank:
        if blank < blank_this:
            break
        candidates_2.append([x, y])


    # 행 작은칸, 열 작은 칸
    candidates_2.sort()
    C[candidates_2[0][0]][candidates_2[0][1]] = num

satisfaction = 0
D.sort()
for x in range(N):
    for y in range(N):
        num = C[x][y]
        likes = [D[num-1][1], D[num-1][2], D[num-1][3], D[num-1][4]]
        temp = 0
        for way in range(4):
            nx, ny = x + dx[way], y + dy[way]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if C[nx][ny] in likes:
                temp += 1
        if temp == 1:
            satisfaction += 1
        elif temp == 2:
            satisfaction += 10
        elif temp == 3:
            satisfaction += 100
        elif temp == 4:
            satisfaction += 1000
print(satisfaction)
