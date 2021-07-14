# 242 유효한 애너그램 easy
# 정렬
# 문자열을 sorted하면 list로 바뀐다. list는 == 비교구문 가능하다.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

