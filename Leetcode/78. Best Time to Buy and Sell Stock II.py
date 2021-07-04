# 그리디 알고리즘
# 122. 주식을 사고 팔기 가장 좋은 시점 II

# 풀이 1
def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                result += prices[i+1]-prices[i]
        return result
      
# 풀이2 Pythonic way
def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))
