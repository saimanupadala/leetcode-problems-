class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # Single characters are palindromes
        for i in range(n):
            dp[i][i] = 1

        # Length of substring
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    low = i + 1
                    high = j - 1

                    while low <= high and s[low] != s[i]:
                        low += 1

                    while low <= high and s[high] != s[i]:
                        high -= 1

                    if low > high:
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 2
                    elif low == high:
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 1
                    else:
                        dp[i][j] = (
                            2 * dp[i + 1][j - 1]
                            - dp[low + 1][high - 1]
                        )
                else:
                    dp[i][j] = (
                        dp[i + 1][j]
                        + dp[i][j - 1]
                        - dp[i + 1][j - 1]
                    )

                dp[i][j] %= MOD

        return dp[0][n - 1]