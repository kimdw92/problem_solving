# 이진탐색
# 가장 적은 시간에 통과할 수 있는, 0 ~ 최대시간 사이에 있는 시간을 이진탐색으로 찾는다
import sys
def solution(n, times):
    if len(times) == 1:
        return times * n
    
    answer = sys.maxsize
    
    left, right = 0, max(times)*n
    while left <= right:
        mid = (left + right) // 2
        passing = 0
        for time in times:
            passing += mid // time
        if passing >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
                   
    return answer
