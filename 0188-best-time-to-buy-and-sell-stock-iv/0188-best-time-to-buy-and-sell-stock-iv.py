class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        dp = [0] * (k + 1)
        best_buy = [-float('inf')] * (k + 1)
        for price in prices:
            for t in range(1, k + 1):
                best_buy[t] = max(best_buy[t], dp[t - 1] - price)
                dp[t] = max(dp[t], best_buy[t] + price)
        return dp[k]
        