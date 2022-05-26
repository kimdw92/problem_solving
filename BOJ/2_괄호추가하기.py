# 16637번: 괄호 추가하기
# 삼성 A형 기출문제
# 완전탐색, 백트래킹, DFS
# eval 함수 : 문자열 수식을 그대로 계산 해줌
# 풀이 아이디어: 괄호를 start에 추가하는 경우와 start+1에 추가하는 경우 2가지로 단순화 해서 탐색

import sys

N = 19
input = '1*2+3*4*5-6*7*8*9*0'

nums, ops = [], []
for k in input:
    nums.append(k) if k.isdigit() else ops.append(k)
len_ops = len(ops)

result = -1 * sys.maxsize
def dfs(value, start):
    #print(value)
    global result

    if start >= len_ops:
        result = max(result, value)
    else:
        # 괄호 x
        start_value = eval(str(value) + ops[start] + nums[start+1])
        dfs(start_value, start + 1)

        # 괄호 o
        if start >= len_ops - 1:
            return
        next_value = eval(str(value) + ops[start] + '(' + nums[start+1] + ops[start+1] + nums[start+2] + ')')
        dfs(next_value, start + 2)

dfs(int(input[0]), 0)
print(result)
