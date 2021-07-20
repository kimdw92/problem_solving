# 424 가장 긴 반복 문자 대체
# 슬라이딩 윈도우
# 투 포인터
# 윈도우의 길이는 줄어들지 않게 한다.
# at most k
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        cnts = collections.Counter()
        for right, char in enumerate(s):
            cnts[char] += 1
            max_temp = max(cnts.values())
            
            # 윈도우안에서 k개보다 많은 문자열을 바꿔야 한다면 가망이 없으니 left 이동
            if (right-left+1 - max_temp) > k:   
                cnts[s[left]] -= 1
                left += 1
        
        return right-left+1
