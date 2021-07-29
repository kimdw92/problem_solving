# My answer
def solution(dartResult):
    answer = 0
    score = []
    digit = ''
    for char in dartResult:
        if char.isdigit():
            digit += char
            continue
        
        if char.isalpha():
            score.append(int(digit))
            digit = ''
            
            if char == 'D':
                score[-1] = score[-1]**2
            elif char == 'T':
                score[-1] = score[-1]**3
            continue
        
        if char == '*':
            score[-1] *= 2
            try:
                score[-2] *= 2
            except:
                print('index is 0') 
        elif char == '#':
            score[-1] = - score[-1]
            
            
        
    answer = sum(score)
    return answer
  
  # 다른 풀이: 문자열 및 자릿수 올림 처리
  def solution(dartResult):
    nums = [0]
    
    for s in dartResult:
        if s == 'S':
            nums[-1] **= 1
            nums.append(0)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif s == '*':
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif s == '#':
            nums[-2] *= -1
        else:
            # 숫자일경우
            nums[-1] = nums[-1] * 10 + int(s)
    return sum(nums)
