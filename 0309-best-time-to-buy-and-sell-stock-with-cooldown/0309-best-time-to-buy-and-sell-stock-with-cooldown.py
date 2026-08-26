class Solution:
    def maxProfit(self, prices):
        hold = -prices[0]
        sell = 0
        rest = 0

        for i in range(1, len(prices)):
            prev_hold = hold
            prev_sell = sell
            prev_rest = rest

            hold = max(prev_hold, prev_rest - prices[i])
            sell = prev_hold + prices[i]
            rest = max(prev_rest, prev_sell)

        return max(sell, rest)
        