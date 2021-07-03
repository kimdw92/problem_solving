# 정렬
def solution(citations):
    if len(citations) == 1:
        return 1
    answer = len(citations)
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if (i+1) > c:
            return i
        
        
    return answer
