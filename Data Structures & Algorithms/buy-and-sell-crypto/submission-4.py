class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r <= len(prices) - 1:
            if prices[r] > prices[l]:
                temp_profit = prices[r] - prices[l]
                if temp_profit > profit:
                    profit = temp_profit
            else:
                l = r
            r += 1


        return profit