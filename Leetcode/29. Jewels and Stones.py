# 해시 테이블 771. Jewels and Stones

# My answer: 리스트로 변환
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        js = list(jewels)
        ss = list(stones)
        count = 0
        for s in ss:
            if s in js:
                count += 1
        return count
      
# 풀이1: 해시 테이블을 이용한 풀이
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.defaultdict(int)
        count = 0
        
        for char in stones:
            freq[char] += 1
        
        for char in jewels:
            if char in freq:
                count += freq[char]
                
        return count
      
# 풀이2: Counter로 계산 생략
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        count = 0
        
        # Counter는 존재하지 않는 키의 경우 0을 출력해준다.
        for char in jewels:
            if char in freq:
                count += freq[char]
                
        return count
      
# 풀이3: 파이썬 다운 방식
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
