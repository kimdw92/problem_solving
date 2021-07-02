# 56. 구간 병합
# 정렬하여 병합
# My answer: 84 ms	16.1 MB
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        result = []
        idx = 1
        for idx, [x, y] in enumerate(intervals):
            if idx == 0:
                start, end = x, y
                continue
            if x <= end and y <= end:
                continue
            elif x <= end and y > end:
                end = y
            elif x > end:
                result.append([start, end])
                start, end = x, y
        result.append([start, end])
                
        return result
      
# 풀이1: 76 ms	16.1 MB
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        
        for i in sorted(intervals, key=lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i,
        return merged
