# My answer
# bin(9) --> 0b1001
def solution(n, arr1, arr2):
    answer = []
    # 한 줄씩 처리
    for i in range(n):
        # 십진수를 이진수로 변환
        arr1_bin, arr2_bin = bin(arr1[i])[2:], bin(arr2[i])[2:]
        if len(arr1_bin) < n:
            for _ in range(n - len(arr1_bin)):
                arr1_bin = '0' + arr1_bin
        if len(arr2_bin) < n:
            for _ in range(n - len(arr2_bin)):
                arr2_bin = '0' + arr2_bin
                
        # 공백인지 샵인지 판단        
        row = ''
        for a, b in zip(arr1_bin, arr2_bin):
            if a == '0' and b == '0':
                row += ' '
            else:
                row += '#'
        answer.append(row)
    return answer
  
# 다른 풀이: 비트 연산자 OR 이용  
# zfill() 문자열 앞에 인수 만큼 0으로 채운다
# replace
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # OR 연산 후 이진수 변환
        answer.append(
        bin(arr1[i] | arr2[i])[2:]
        .zfill(n)
        .replace('1', '#')
        .replace('0', ' '))
    return answer
