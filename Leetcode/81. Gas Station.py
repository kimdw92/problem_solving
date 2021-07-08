# 그리디..?
# 134 주유소

# O(n) / sum(gas)가 sum(cost)보다 크다면, 반드시 솔루션이 존재 64 ms	15.1 MB
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 기름은 충분한가? 충분하다면 반드시 솔루션이 존재한다.
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발이 안되는 지점
            if fuel + gas[i] < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start
      
# O(n^2) / My answer: brute-force 4840 ms	15.2 MB
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Brute-force
        answer = -1
        for i in range(len(gas)):
            have = 0
            for j in range(i, i+len(gas)+1):
                if j == (i+len(gas)):
                    return i
                idx = j % len(gas)
                have += gas[idx]
                if have < cost[idx]:
                    break
                have -= cost[idx]
        return answer
