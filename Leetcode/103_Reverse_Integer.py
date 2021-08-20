# 7 Reverse Integer
# Easy
# My answer
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            prefix = '-'
            x = -x
        else:
            prefix = ''
            
        str_x = str(x)
        list_str_x = list(str_x)
        list_str_x.reverse()
        # 앞자리에 0 이 있으면 제거
        for idx, char in enumerate(list_str_x):
            if char != '0':
                list_str_x = list_str_x[idx:]
                break
        result = ''.join(list_str_x)
        
        # 32비트 정수가 아닌지 체크
        if int(result) < -2**31 or int(result) > 2**31 -1:
            return 0
        return prefix + result
