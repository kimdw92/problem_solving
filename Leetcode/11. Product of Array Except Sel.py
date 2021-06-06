# 배열11 자신을 제외한 배열의 곱
# 시간복잡도 O(n), O(1)으로 풀이하는 방법 찾기

# My answer, 공간복잡도 fail
def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l == 2:
            nums.reverse()
            return nums
    
        extended = []
        answer = collections.defaultdict(lambda: 1)
        for i in range(l):
            temp = nums.pop(i)
            extended.extend(nums)
            nums.insert(i, temp)
        idx = 0
        for i in range(len(extended)):
             
            answer[idx] *= extended[i]
            if (i+1) > 0 and (i+1) % (l-1) == 0:
                idx += 1
        return answer.values()
      
# 풀이1 왼쪽 곱셈, 오른쪽 곱셈 따로 구하는 방법
# 거꾸로 탐색: range(len(nums)-1, 0-1, -1)
def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(len(nums)):
            out.append(p)
            p *= nums[i]
        p = 1
        # 오른쪽 곱셈
        for i in range(len(nums)-1, 0-1, -1):
            out[i] *= p
            p *= nums[i]
        return out
