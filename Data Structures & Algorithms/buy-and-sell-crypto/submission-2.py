class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        sell = 0
        for price in prices[1:]:
            if price < buy:
                buy = price
                sell = price
            elif price > sell:
                sell = price

            max_profit = max(max_profit,sell-buy)
        return max_profit

