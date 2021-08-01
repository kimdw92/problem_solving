# Counter를 이용한 구현
# https://programmers.co.kr/learn/courses/30/lessons/17677

# 좀 더 간결한 풀이
# Counter의 합집합과 교집합 이용
def solution(str1, str2):
    # 다중 집합 생성(리스트 컴프리헨션)
    str1s = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2s = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    str1s_cnt = collections.Counter(str1s)
    str2s_cnt = collections.Counter(str2s)
    
    # 교집합 계산
    intersection = sum((str1s_cnt & str2s_cnt).values())
    
    # 합집합 계산
    union = sum((str1s_cnt | str2s_cnt).values())
    
    jaccard_sim = 1 if union == 0 else intersection / union
    return int(jaccard_sim * 65536)
  
# My answer
import collections
def solution(str1, str2):
    # 다중 집합 생성 함수
    def get_list(str_input):
        str_set = []
        for i in range(len(str_input)-1):
            first, second = str_input[i], str_input[i+1]
            if first.isalpha() and second.isalpha():
                first = first.lower()
                second = second.lower()           
                str_set.append(first+second)
        return str_set
    
    str1_list = get_list(str1)
    str2_list = get_list(str2)
    
    # 자카드 유사도
    str1_cnt = collections.Counter(str1_list)
    str2_cnt = collections.Counter(str2_list)
    
    inter, union = 0, 0
    for str1_key in str1_cnt.keys():
        if str1_key in str2_cnt.keys():
            inter += min(str1_cnt[str1_key], str2_cnt[str1_key])
            union += max(str1_cnt[str1_key], str2_cnt[str1_key])
        else:
            union += str1_cnt[str1_key]
            
    for str2_key in str2_cnt.keys():
        if str2_key not in str1_cnt.keys():
            union += str2_cnt[str2_key]
            
            
    if inter == 0 and union == 0:
        similarity = 1
    else:
        similarity = inter / union
    
    return int(similarity * 65536)
  
