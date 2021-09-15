# My answer
# 완전탐색, 시간초과
def str2sec(string):  
    """ 시간 문자열을 초로 바꿔서 int로 반환 """
    
    hour, min, sec = map(int, string.split(':'))
    return hour * 3600 + min * 60 + sec

def solution(play_time, adv_time, logs):
    # 초단위로 변환
    pt = str2sec(play_time)
    at = str2sec(adv_time)
    
    if pt == at:
        return "00:00:00"
    
    # logs도 초단위로 변환해서 저장
    logs_2 = []
    for log in logs:
        start, end = log.split("-")
        start = str2sec(start)
        end = str2sec(end)
        
        logs_2.append([start, end])
        
    logs_2.sort()
    max_count = 0
    answer = [0, at]
    for i in range(len(logs_2)):
        start, end = logs_2[i][0], logs_2[i][1]
        adv_start, adv_end = start, start + at
        count = end - start if end <= adv_end else at
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

# 공식 풀이
# https://dev-note-97.tistory.com/156
# Memoization... DP수럽게
# 실제 시험 때 바로 이런 아이디어를 어떻게 생각하니?
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)        # 1
    adv_time = str_to_int(adv_time)               
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                           # 2
        start, end = l.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):       # 3
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):       # 4
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                           # 5
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)


def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s
