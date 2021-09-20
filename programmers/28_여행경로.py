# level 3
# DFS, 백트래킹
# 리스트를 구하기 위해서, 인자에 넣어주기
# path를 복사해야 값이 안바뀐다
# 백트래킹을 위한 path 초기화 주의

import collections
def solution(tickets):
    answer = []
    length = len(tickets)
    ts = collections.defaultdict(list)
    for start, end in tickets:
        ts[start].append(end)
    
    def dfs(arrival, path, ts, count, answer):
        path.append(arrival)
        if count == length:
            answer.append(path[:]) # path를 복사해야 값이 안바뀐다
            return        
        
        for idx, next_end in enumerate(ts[arrival]):
            if next_end == True:
                continue
            ts[arrival][idx] = True
            dfs(next_end, path, ts, count+1, answer)
            ts[arrival][idx] = next_end
            
            # 백트래킹! 위의 dfs안에서의 path 변화를 되돌리기 위함
            path.pop()
    
    dfs('ICN',[], ts, 0, answer)
    return sorted(answer)[0]
