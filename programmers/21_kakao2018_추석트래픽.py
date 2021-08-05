# 슬라이딩윈도우
# 너무 어려운데..?

import datetime
def solution(lines):
    combined_logs = []
    # datetime 문자열 형태를 타임스탬프로 변환
    # 시작시간과 종료시간을 튜플형태로 저장
    for log in lines:
        logs = log.split()
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))
        
    accumulated = 0
    max_requests = 1
    combined_logs.sort(key=lambda x: x[0])
    for i, elem1 in enumerate(combined_logs):
        current = accumulated
        
        # 1초 미만 윈도우 범위 요청 수 계산
        for elem2 in combined_logs[i:]:
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += 1
                
        max_requests = max(max_requests, current)
        accumulated += elem1[1]
                             
    return max_requests
