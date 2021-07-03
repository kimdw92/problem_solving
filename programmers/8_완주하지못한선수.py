# 해시
import collections
def solution(participant, completion):
    answer = ''
    p_cnt = collections.Counter(participant)
    c_cnt = collections.Counter(completion)
    for name in participant:
        if p_cnt[name] != c_cnt[name]:
            answer = name
    return answer
