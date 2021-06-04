# 04 가장 흔한 단어
# 문자열 조작
# 정규 표현식 words = [word for word in re.sub(r'[^\w]', ' ', paragraph) : 리스트 컴프리헨션!!!
#               .lower().split() if word not in banned]
# \w는 word character이고 ^는 not을 의미한다. 문자가 아닌 것을 공백으로 치환한다는 뜻

# counts = collections.Counter(words) : Counter 모듈이 자동으로 갯수를 세준다
# return counts.most_common(1)[0][0] : 인덱싱 없으면 [('ball', 2)]가 출력 됨

# counts = collections.defaultdict(int) : 자동으로 int=0의 key를 생성해주는 딕셔너리 모듈
# return max(counts, key=counts.get) : argmax와 같은 효과

# Answer 1 : Counter 모듈
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Data Cleansing
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫번째 인덱스 리턴
        return counts.most_common(1)[0][0] # 인덱싱 없으면 [('ball', 2)]가 출력 됨
      
# Answer 2 : defaultdict 모듈
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Data Cleansing
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split() if word not in banned]
        
        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1
            
        return max(counts, key=counts.get)
            
