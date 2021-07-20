# 76 부분 문자열이 포함된 최소 윈도우
# 슬라이딩 윈도우
# 투 포인터, 좌우 포인터를 좁혀가면서 오른쪽으로 이동
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        # right를 오른쪽으로 이동
        for right, char in enumerate(s):
            missing -= need[char] > 0
            need[char] -= 1
                
            # left를 오른쪽으로 이동
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                    
                if not end or (right+1)-left <= end-start:
                    start, end = left, right+1
                    
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
