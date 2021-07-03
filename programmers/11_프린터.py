# 스택
def solution(priorities, location):
    if len(priorities) == 1:
        return 1
    
    answer = 0
    data = [[i, p] for i, p in enumerate(priorities)]
        
    while True:
        i, p = data.pop(0)
        answer += 1
        if_print = True
        for other_i, other_prior in data:
            if other_prior > p:
                data.append([i, p])
                answer -= 1
                if_print = False
                break
                
        if if_print and i == location:
            break
        
        
    return answer
