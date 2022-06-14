# 23291 어항정리
# 플래티넘5
# 구현 시뮬레이션
# 풀이방법이 떠오르지 않아 타 코드 참고
# Input의 요소를 2Dlist형태로 저장
# 2D matrix 떼어내서 회전
# 회전을 위한 padding

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, K = map(int, input().split())
fishes = list(map(int, input().split()))
grounds = [[fish] for fish in fishes]
result = 0

# 시계방향 행렬회전
def rotate(x, y):
    temp = [[0] * x for _ in range(y)]
    for r in range(x):
        for c in range(y):
            temp[c][x - r - 1] = selected[r][c]
    return temp

# 어항정리
def control_fish():
    x_len = len(grounds)
    y_len = len(grounds[0])
    _temp = [[0] * y_len for _ in range(x_len)]
    for x in range(x_len):
        for y in range(y_len):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if grounds[x][y] == -1:
                    continue
                if nx < 0 or nx >= x_len or ny < 0 or ny >= y_len or grounds[nx][ny] == -1:
                    continue
                diff = grounds[x][y] - grounds[nx][ny]
                if diff >= 5:
                    d = diff // 5
                    _temp[x][y] -= d
                    _temp[nx][ny] += d
    for x in range(x_len):
        for y in range(y_len):
            grounds[x][y] += _temp[x][y]

# 일렬로 놓기
def vectorize():
    x_len = len(grounds)
    y_len = len(grounds[0])
    result = []
    for x in range(x_len):
        for y in range(y_len):
            if grounds[x][y] == -1:
                continue
            result.append([grounds[x][y]])
    return result




while True:
    minimum = 1e9
    maximum = -1e9
    for ground in grounds:
        minimum = min(minimum, ground[0])
        maximum = max(maximum, ground[0])
    if maximum - minimum <= K:
        break
    result += 1

    # 최소인 어항에 물고기 추가
    for i in range(len(grounds)):
        if grounds[i][0] == minimum:
            grounds[i][0] += 1

    #print('물고기추가', grounds)
    # 가장 왼쪽 어항 들어올리기
    left_1 = grounds.pop(0)
    grounds[0].extend(left_1)

    #print('하나 올리기', grounds)
    # 2개 이상 쌓인 어항 김밥말이
    while True:
        # 2개 이상 쌓인 어항 확인
        idx = 0
        while len(grounds[idx]) >= 2:
            idx += 1
            if len(grounds) - idx < len(grounds[0]):
                break

        if len(grounds) - idx < len(grounds[0]):
            break

        # 선택된 어항 회전
        selected = list()
        for _ in range(idx):
            selected.append(grounds.pop(0))
        rotated_selected = rotate(idx, len(selected[0]))

        # 어항 올리기
        for i in range(len(rotated_selected)):
            grounds[i].extend(rotated_selected[i])

        #print('김밥말이', grounds)

    # 편의를 위해 (-1) padding
    height = len(grounds[0])
    for i in range(len(grounds)):
        while len(grounds[i]) < height:
            grounds[i].append(-1)

    #print('padding', grounds)

    # 물고기 수 조절절
    control_fish()
    #print('물고기조절', grounds)
    # 다시 어항을 바닥에 일렬로 놓기
    grounds = vectorize()
    #print('일렬로', grounds)

    # 다시 절반씩 공중부양 x2
    for _ in range(2):
        mid = len(grounds) // 2
        selected = list()
        for _ in range(mid):
            selected.append(grounds.pop(0))
        for i in range(mid):
            step = selected.pop()
            step.reverse()
            grounds[i].extend(step)
        #print('공중부양', grounds)

    # 다시 물고기 수 조절 & 일렬로 놓기
    control_fish()
    #print('물고기조절', grounds)
    grounds = vectorize()
    #print('결과', grounds)

print(result)
