# level 4? 너무 어려어~
# 구현
# bfs
# 90도 회전
# 좌표 0,0 기준 통일하기
# 참고: https://ye333.tistory.com/163
import collections

# bfs로 블록 모양 list 저장 함수
def bfs(i, j, board, visited, empty, n):
    section = []
    q = collections.deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        if x >= 0 and y >= 0:
            try:
                if visited[x][y] == False and board[x][y] == n:
                    visited[x][y] = True
                    section.append((x, y))
                    q.append((x - 1, y))
                    q.append((x + 1, y))
                    q.append((x, y - 1))
                    q.append((x, y + 1))
            except IndexError:
                continue
    empty.append(sorted(section))


def standard_0(b):
    tmp = []
    std_x, std_y = b[0][0], b[0][1]
    for x, y in b:
        tmp.append((x - std_x, y - std_y))
    return tmp


def solution(game_board, table):
    N = len(game_board)

    visited_board = [[False] * N for _ in range(N)]
    empty_board = []  # game_board의 빈 좌표

    visited_table = [[False] * N for _ in range(N)]
    block_table = []

    # game_board의 빈 좌표를 empty_board에 저장
    for i in range(N):
        for j in range(N):
            if visited_board[i][j] == False and game_board[i][j] == 0:
                bfs(i, j, game_board, visited_board, empty_board, 0)

    # table의 블록 좌표를 block_table에 저장
    for i in range(N):
        for j in range(N):
            if visited_table[i][j] == False and table[i][j] == 1:
                bfs(i, j, table, visited_table, block_table, 1)

    # block_table의 좌표를 (0, 0) 기준으로 변경 (?)
    blocks = []
    for block in block_table:
        blocks.append(standard_0(block))
    emptys = []
    for empty in empty_board:
        emptys.append(standard_0(empty))

    # 블록 90도 시계방향 회전 함수
    def rotate(block):
        new = []
        for x, y in block:
            new.append((y, N - 1 - x))
        return standard_0(sorted(new))

    answer = 0
    used_blocks = [False] * len(blocks)

    for empty in emptys:
        find = 0
        for idx, block in enumerate(blocks):
            if used_blocks[idx]:  # 이미 사용한 블럭이면 스킵
                continue
            if len(empty) != len(block):
                continue
            for _ in range(4):
                if empty == block:
                    used_blocks[idx] = True
                    answer += len(block)
                    find = 1
                    break
                else:
                    block = rotate(block)
            if find > 0: break
    return answer
