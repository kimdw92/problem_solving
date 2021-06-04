# 로그 파일 재정렬
# 람다 표현식
# 람다는 간단한 함수를 한줄로 정의할 때 사용 가능하다
# sort(key = func) : key에 함수로 입력이 가능하고 우선순위는 순서로 반영 ex) func = (x[0], x[1])
# log.split()[1] : .split은 공백을 기준으로 string을 쪼개서 list로 변환

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
