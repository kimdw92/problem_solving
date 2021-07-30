# LRU 알고리즘은 deque(maxlen=) 으로 구현 가능
# 캐시 히트: 캐시에 이미 존재할 경우
# 캐시 미스: 캐시에 없을 경우
import collections
def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque(maxlen=cacheSize)
    
    for c in cities:
        c = c.lower()
        # 캐시 히트 시 재삽입
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else: # 캐시 미스 시 삽입만
            cache.append(c)
            answer += 5
    return answer
