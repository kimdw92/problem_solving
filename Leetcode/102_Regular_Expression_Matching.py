# 재귀를 이용한 풀이
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        
        # 첫 문자 일치 여부
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        # 패턴의 다음문자가 *이면
        if len(p) >= 2 and p[1] == '*':
            # 첫 문자가 일치 안하면 *를 이용해 패턴 첫글자 무시
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
                    # 첫문자가 일치하면 *를 계속 살려두면서 s의 다음 문자 비교
                    
        # 패턴의 다음 문자가 *가 아니면
        else:
            # 그냥 다음 문자 비교
            return first_match and self.isMatch(s[1:], p[1:])
