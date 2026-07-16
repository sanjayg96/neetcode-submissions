class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) < 2:
            return profit
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
            elif prices[sell] > prices[buy]:
                diff = prices[sell] - prices[buy]
                if diff > profit:
                    profit = diff
                sell += 1
            else:
                sell += 1

        return profit