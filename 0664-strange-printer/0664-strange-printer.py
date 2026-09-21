class Solution:
    def strangePrinter(self, s):
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Print s[j] separately
                dp[i][j] = dp[i][j - 1] + 1

                for k in range(i, j):
                    if s[k] == s[j]:
                        left = dp[i][k - 1] if k > i else 0
                        dp[i][j] = min(
                            dp[i][j],
                            left + dp[k][j - 1]
                        )

        return dp[0][n - 1]