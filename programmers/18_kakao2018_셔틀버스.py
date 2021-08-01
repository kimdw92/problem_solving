# 문제 자체를 이해하기에도 쉽지 않다
# https://programmers.co.kr/learn/courses/30/lessons/17678
# 문자열 전처리 및 대기 시각 처리
def solution(n, t, m, timetable):
    # 입력값 분 단위 전처리
    timetable = [
        int(time[:2]) * 60 + int(time[3:]) for time in timetable
    ]
    timetable.sort()
    
    current = 540 # 09:00
    
    for _ in range(n):
        for _ in range(m):
            # 대기가 있는 경우
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else: # 대기가 없는 경우
                candidate = current
        current += t
        
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)
