class Solution:
    def kInversePairs(self, n, k):
        MOD = 10**9 + 7

        dp = [0] * (k + 1)
        dp[0] = 1

        for num in range(1, n + 1):
            new_dp = [0] * (k + 1)
            window = 0

            for j in range(k + 1):
                window += dp[j]

                if j >= num:
                    window -= dp[j - num]

                window %= MOD
                new_dp[j] = window

            dp = new_dp

        return dp[k]