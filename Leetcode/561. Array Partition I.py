# 10 배열
# 배열 파티션1

# My answer: 짝수 번째 값 계산 276 ms	16.6 MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        result = 0
        for i in range(1, len(nums), 2):
            result += nums[i]
        return result
    
    
# 풀이1: 오름차순 풀이 288 ms	16.9 MB
# 내 풀이랑 원리는 같은데 pair 변수를 이용한 테크닉에 주목
def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()
        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum
    
# 풀이2: 짝수 번째 값 계산 376 ms	16.9 MB
# 내 풀이랑 원리는 같은데 enumerate를 이용한 테크닉에 주목
def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()
        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n
                
        return sum
    
# 풀이3: 파이썬 다운 방식
# 슬라이싱
def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
