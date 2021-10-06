# level 2
# 트리, 완전탐색
# My answer
import collections
def solution(n, wires):
    # 트리, 완전탐색?
    answer = 1e9
    dict = collections.defaultdict(list)
    for v1, v2 in wires:
        dict[v1].append(v2)
        dict[v2].append(v1)
    
    def dfs(node, cnt, visited):
        if len(dict[node]) == 0:
            return cnt
        
        for next_node in dict[node]:
            if next_node in visited:
                continue
            cnt += 1
            visited.append(next_node)
            cnt = dfs(next_node, cnt, visited)
        
        return cnt
        
    for v1, v2 in wires:
        dict[v1].remove(v2)
        dict[v2].remove(v1)
        num1 = dfs(v1, 1, [v1])
        num2 = dfs(v2, 1, [v2])
        answer = min(answer, abs(num1-num2))
        dict[v1].append(v2)
        dict[v2].append(v1)
        
    return answer
