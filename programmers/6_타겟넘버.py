# DFS
# 변수 재할당을 위해 global 선언
answer = 0
def solution(numbers, target):
    global answer
    ops = [-1, 1]
    
    def dfs(_sum, idx):
        global answer
        if idx >= len(numbers):
            if _sum == target:
                answer += 1
                return
            else:
                return
        for op in ops:
            add = numbers[idx] * op
            _sum += add
            dfs(_sum, idx+1)
            _sum -= add
            
    dfs(0, 0)
    return answer
