# 문자열 조작
# 유효한 팰린드롬

# 숫자, 알파벳 확인: .isdigit() .isalpha() .isalnum()
# string 소문자로 변환: .lower()
# 정규식으로 숫자, 알파벳만 남기기: s = re.sub('[^a-z0-9]', '', s)

# 슬라이싱 참고
# s[:] 사본 리턴
# s[::-1] 뒤집기
# s[::2] 2칸씩 앞으로

# My answer, 44 ms	15.7 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        original_s = []
        reversed_s = []
        s = s.lower()
        for word in s:
            if word.isdigit() or word.isalpha():
                original_s.append(word)
                reversed_s.append(word)
    
        reversed_s.reverse()
        if reversed_s == original_s:
            return True
        else:
            return False

# 풀이1 리스트로 변환 292 ms	19.6 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True
      
# 풀이2 deque 자료형 48 ms	19.2 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
        
# 풀이3 정규식, 슬라이싱   40 ms	15.5 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1] # 슬라이싱
