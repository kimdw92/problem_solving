# 07 두수의 합
# 최적화 하는 여러가지 방법이 존재

# 풀이1 Brute-force 4228 ms	14.9 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                  
# 풀이 2 in을 이용한 탐색   652 ms	14.7 MB
# complement가 in 인지 탐색
# in 함수는 for처럼 O(n) 이긴하지만 상수항때문에 더 빠르다.
# nums.index(n) : nums 리스트에서 n의 인덱스를 리턴
def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + i+1]
              
# 풀이3 딕셔너리 키 조회 52 ms	15.3 MB
# 딕셔너리는 해시 테이블로 구현되어 있고, 이 경우 조회는 평균적으로 O(1)에 가능하다. (최악은 O(n))
# targetr - num in nums_map : 키 값을 조회
def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target-num]]
              
# 풀이4 풀이3의 for를 하나로 단순화, 60 ms	15.4 MB
def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i
            
# 풀이4 투포인터, 인덱스를 묻는 문제라 이 방법을 사용할 수는 없지만..
# left와 right을 양 끝에 박고 시작해서 값이 크면 right-=1, 작으면 left+=1
def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while not left == right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
