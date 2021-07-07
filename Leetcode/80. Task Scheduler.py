# 621 태스크 스케줄러
# 그리디
# Counter모듈의 most_common, subtract 사용
# most_common(n+1) 씩 불
# Counter 0 이하 아이템 제거 : counter += collections.Counter()
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            subcnt = 0
            for task, _ in counter.most_common(n+1):
                subcnt += 1
                result += 1
                
                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전 제거
                counter += collections.Counter()
                
            if not counter:
                break
                
            result += n - subcnt + 1
            
        return result
