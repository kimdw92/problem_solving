# DFS, 완전탐색
# level 3
def solution(begin, target, words):
    if target not in words:
        return 0
    
    def dfs(word, visited, count):
        if word == target:
            nonlocal answer
            answer = min(answer, count)
            return
        
        for i in range(len(word)):
            for j, word2 in enumerate(words):
                if visited[j] == 0 and word[:i] + word[i+1:] == word2[:i] + word2[i+1:]:
                    visited[j] = 1
                    dfs(word2, visited, count+1)
                    visited[j] = 0
        
        
        
    answer = 1e9
    visited = [0] * len(words)
    dfs(begin, visited, 0)
    
    return answer
