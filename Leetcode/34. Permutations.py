# 46. 순열

# My asnwer: DFS
# 리스트는 객체이고 파이썬에서 객체는 참조되는 형태로 처리된다. append할 때 copy해서 삽입해야함.
def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(temp):
            if len(nums) == len(temp):
                # 리스트 객체는 참조하는 형태이므로 값이 바뀌지 않도로 복사하는 형태로 삽입한다.
                result.append(temp[:])
                return
              
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    dfs(temp)
                    temp.pop()
        dfs([])
        return result
      
# 풀이1: itertools 모듈 사용
def permute(self, nums: List[int]) -> List[List[int]]:
        # permutations()함수의 출력은 튜플이다. 리스트로 변환하려면 아래
        # return list(map(list,itertools.permutations(nums)))
        return list(itertools.permutations(nums))
