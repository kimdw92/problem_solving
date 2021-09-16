# 복잡한 구현 문제
# deque를 이용한 bfs로 최단거리 구하기
# 완전탐색인 요소도 존재
# 
import collections  
from itertools import permutations
from copy import deepcopy

temp_board = []
def ctrl_move(r, c, dr, dc):
    global temp_board
    while True:
        nr, nc = r + dr, c + dc
        if not (0<=nr<4 and 0<=nc<4):
            return r, c
        if temp_board[nr][nc] > 0:
            return nr, nc
        r, c = nr, nc


# bfs로 거리 구하기
def bfs(start, end):
    r, c = start
    target_r, target_c = end
    q = collections.deque()
    q.append((r, c, 0))
    visited = [[0] * 4 for _ in range(4)]
    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while q:
        r, c, temp = q.popleft()
        if visited[r][c]: continue
        visited[r][c] = 1
        if r == target_r and c == target_c:
            return temp
        
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0<=nr<4 and 0<=nc<4:
                q.append((nr, nc, temp+1))
            nr, nc = ctrl_move(r, c, dr, dc)
            q.append((nr, nc, temp+1))
    return -1
  
    
def solution(board, r, c):
    global temp_board    
    pairs = collections.defaultdict(list)
    nums = []
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                if board[i][j] not in nums:
                    nums.append(board[i][j])
                pairs[board[i][j]].append([i, j]) # pairs[1][0] = [0, 0]
    per = list(permutations(nums, len(nums)))
    answer = 1e9
    
    # 6가지 경우의수 '123', '132', '213' ...
    for i in range(len(per)):
        temp_board = deepcopy(board)
        _r, _c = r, c
        cnt = 0
        for card in per[i]:
            # 같은 그림의 카드 2장중 가까운 카드로 간다
            first = bfs((_r, _c), pairs[card][0])
            second = bfs((_r, _c), pairs[card][1])
            if first < second:
                cnt += first
                cnt += bfs(pairs[card][0], pairs[card][1])
                _r, _c = pairs[card][1]
            else:
                cnt += second
                cnt += bfs(pairs[card][1], pairs[card][0])
                _r, _c = pairs[card][0]
            cnt += 2 # enter * 2
            # 카드 지우기
            for remove_r, remove_c in pairs[card]:
                temp_board[remove_r][remove_c] = 0
                
        answer = min(answer, cnt)
    return answer
