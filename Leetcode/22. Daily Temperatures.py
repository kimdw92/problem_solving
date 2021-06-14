# 스택, 큐 22: 일일 온도

# 스택 값 비교
# 이전 날 보다 기온이 높아지면 pop() 하고 아니라면 스택 쌓아서 다음 스텝으로
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):  
            # 현재 온도가 스택 값보다 높다면 result 업데이트
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                result[idx] = i - idx                
            stack.append(i)
  
        return result
