# Hard, 239. 최대 슬라이딩 윈도우
# max를 안쓰는 방법으로 풀어야 time-limit에 안걸려
# deque이용
# window에 추가되는 값보다 작은 값은 삭제 하는 방식
# 들어오고 나가는 순서를 실제로 적어보자
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1] 3
        # [3] -1
        # [3, -1] -3
        # [3, -1, -3] 5
        # [5] 3
        # [5 3] 6
        # [6] 7
        # [7]
        
        results = []
        # q는 index를 담으며, 새로운 index보다 작은 요소는 삭제된다.
        q = collections.deque()
        
        for i, n in enumerate(nums):
            # 최댓값이 지금 턴에 빠질 index라면 삭제
            if q and (i - q[0]) == k:
                q.popleft()
                
            # 이번 턴의 n보다 작은 요소들은 삭제
            while q and nums[q[-1]] < n:
                q.pop()
                
            q.append(i)
            
            if i >= k-1:
                results.append(nums[q[0]])
                
        return results
