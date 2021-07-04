# greedy
def solution(n, lost, reserve):
    answer = n
    lost_update = []
    for l in lost:
        if l in reserve:
            reserve.pop(reserve.index(l))
            continue
        lost_update.append(l)
    for l in lost_update:
        if l-1 in reserve:
            reserve.pop(reserve.index(l-1))
            continue
        elif l in reserve:
            reserve.pop(reserve.index(l))
            continue
        elif l+1 in reserve:
            reserve.pop(reserve.index(l+1))
            continue
        answer -= 1
    
    return answer
