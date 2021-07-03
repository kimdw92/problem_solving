# 스택
import math
def solution(progresses, speeds):
    answer = []
    remain = []
    for p, s in zip(progresses, speeds):
        remain.append(math.ceil((100 - p) / s))
    
    prev = 0
    for d in remain:
        if prev < d:
            answer.append(1)
            prev = d
        else:
            answer[-1] += 1    
        
    return answer
