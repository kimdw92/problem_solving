# 카테고리는 해쉬인데... 이 풀이가 더 나은듯
# sort() 문자열정렬은 '1', '12', '123', '56' 이런식이다
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            return answer
    return answer
