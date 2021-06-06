# 배열 12 주식을 사고팔기 가장 좋은 시점
# O(n)으로 가능하다. (카데인 알고리즘?)
def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize # 시스템의 가장 큰 값
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
