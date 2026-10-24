
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            for members in range(n, g - 1, -1):
                for pr in range(minProfit, -1, -1):
                    new_profit = min(minProfit, pr + p)
                    dp[members][new_profit] = (
                        dp[members][new_profit] + dp[members - g][pr]
                    ) % MOD

        return sum(dp[members][minProfit] for members in range(n + 1)) % MOD
