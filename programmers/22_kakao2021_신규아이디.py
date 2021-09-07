# 1번

# My answer
# 정규표현식
import re
def solution(new_id):
    m = len(new_id)
    # step1 소문자로 치환
    new_id = new_id.lower()
    
    # step2 알파벳, 숫자, -, _, .를 제외한 문자 제거
    new_id = re.sub('[^0-9a-z-_.]', '', new_id)
    
    # step3 .. -> .
    new_id = re.sub(r'([.])\1+', r'\1', new_id)
    
    # step4 처음과 끝의 . 제거
    if len(new_id) > 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id == '.':
        new_id = ''
    
    # step5 빈 문자열이라면, a를 대입
    if len(new_id) == 0:
        new_id = 'a'
        
    # step6 16자 이상이면 줄이기
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    
    # step7 2자 이하라면, 반복
    if len(new_id) <= 2:
        m = len(new_id)
        new_id = new_id + new_id[-1] * (3 - m)
    
    return new_id
  
# 다른풀이
# 정규표현식 공부
import re
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st) # a-z, 0-9, -, _, . 만 남기기
    st = re.sub('\.+', '.', st) # .. -> .
    st = re.sub('^[.]|[.]$', '', st) # 맨앞과 맨뒤의 . 제거
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
