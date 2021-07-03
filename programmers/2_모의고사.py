# 완전탐색
import collections
def solution(answers):
    if answers == []:
        return []
    
    pick = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    index = [None, None, None]
                                     
    answer = collections.defaultdict(int)
    for i in range(len(answers)):
        index[0] = i % 5
        index[1] = i % 8
        index[2] = i % 10
        for j in range(3):
            if answers[i] == pick[j][index[j]]:
                answer[j] += 1
                
    max_score_key, max_score_value = max(answer.items(), key = lambda x: x[1])            
    result = []
    for k, v in answer.items():
        if v == max_score_value:
            result.append(k+1)
    result.sort()
    return result
