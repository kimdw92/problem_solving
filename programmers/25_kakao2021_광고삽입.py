# 푸는중
def solution(play_time, adv_time, logs):
    # 초단위로 변환
    h, m, s = play_time.split(':')
    pt = int(h) * 3600 + int(m) * 60 + int(s)
    h, m, s = adv_time.split(':')
    at = int(h) * 3600 + int(m) * 60 + int(s)
    
    if pt == at:
        return "00:00:00"
    
    # logs도 초단위로 변환해서 저장
    logs_2 = []
    for log in logs:
        start, end = log.split("-")
        h, m, s = start.split(":")
        start = int(h) * 3600 + int(m) * 60 + int(s)
        h, m, s = end.split(":")
        end = int(h) * 3600 + int(m) * 60 + int(s)
        
        logs_2.append([start, end])
        
    logs_2.sort()
    max_count = 0
    answer = [0, at]
    for i in range(len(logs_2)):
        start, end = logs_2[i][0], logs_2[i][1]
        adv_start, adv_end = start, start + at
        count = end - start if end - start < at else at
        for j in range(i+1, len(logs_2)):
            _start, _end = logs_2[j][0], logs_2[j][1]
            if _start >= adv_end:
                break
            count += _end - _start if _end <= adv_end else adv_end - _start
        if count > max_count:
            max_count = count
            answer = [adv_start, adv_end]
            
        
    if answer[1] > pt:
        answer[0] = answer[0] - (answer[1] - pt)
        
    m, s = divmod(answer[0], 60)
    h, m = divmod(m, 60)
    answer_2 = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)
    return answer_2
