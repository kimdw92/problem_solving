# 이진탐색
# 무엇을 이진탐색할것이냐... -> min_distance
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 0, distance
    rocks.append(distance)
    
    while left <= right:
        # 거리의 최솟값
        mid = (left + right)//2
        removed = 0
        mins = float('inf')
        prev = 0
        for rock in rocks:
            if rock - prev < mid:
                removed += 1
            else:
                mins = min(mins, rock-prev)
                prev = rock
        
        if removed > n:
            right = mid - 1
        else:
            answer = mins
            left = mid + 1
    return answer
