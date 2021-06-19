# 3. 중복 문자 없는 가장 긴 부분 문자열

# My answer: 해시테이블을 이용한 brute-force, 느림, 804 ms	14.5 MB
def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        length = 1
        # s_list = list(s)
        for i in range(l-1):
            temp = collections.defaultdict(int)
            temp[s[i]] += 1
            for j in range(i+1, l):
                if temp[s[j]] > 0:
                    break
                temp[s[j]] += 1
            if len(temp) > length:
                length = len(temp)
            
        return length
      
# 풀이1: 슬라이딩 윈도우와 투 포인터로 사이즈 조절, 훨씬 빠름       40 ms	14.5 MB
def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index-start+1)
                
            used[char] = index
            
        return max_length
