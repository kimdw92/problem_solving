# 백준 17471 게리맨더링
# 삼성A형 기출
# 완전탐색
# 선거구 조합은 combinations으로 구한다.
# 선거구 조합을 DFS로 구하려다가 실패... 그래프 연결에서 DFS/BFS로 조합을 구할수 없는가?

N = int(input())
P = list(map(int, input().split()))
D = []
def minus(n):
    return int(n) - 1
for _ in range(N):
    D.append(list(map(minus, input().split())))

from collections import deque
import itertools

def check_connect(b_list):
    q = deque()
    q.append(b_list[0])
    connect = []
    connect.append(b_list[0])
    while q:
        node = q.popleft()
        for naver in D[node][1:]:
            if naver in b_list and naver not in connect:
                q.append(naver)
                connect.append(naver)
    return len(connect), sum([P[i] for i in connect])

ab_pop = sum(P)
answer = 1e9
for i in range(1, N//2 + 1):
    candidates = list(itertools.combinations(range(N), i))
    for candidate in candidates:
        other = [i for i in range(N) if i not in candidate]
        a_len, a_sum = check_connect(candidate)
        b_len, b_sum = check_connect(other)
        if a_len + b_len == N:
            answer = min(answer, abs(a_sum-b_sum))

if answer == 1e9:
    print(-1)
else:
    print(answer)
    
'''
추가 테스트 케이스
8
17 42 46 81 71 8 37 12
4 2 4 5 7
5 1 3 4 5 8
2 2 4
5 1 2 3 7 8
5 1 2 6 7 8
2 5 8
4 1 4 5 8
5 2 4 5 6 7
OUTPUT: 2
'''
