class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = number of ways to reach cell (i, j)
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1

        answer = 0

        for _ in range(maxMove):
            new_dp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if dp[i][j] == 0:
                        continue

                    # Up
                    if i == 0:
                        answer = (answer + dp[i][j]) % MOD
                    else:
                        new_dp[i - 1][j] = (new_dp[i - 1][j] + dp[i][j]) % MOD

                    # Down
                    if i == m - 1:
                        answer = (answer + dp[i][j]) % MOD
                    else:
                        new_dp[i + 1][j] = (new_dp[i + 1][j] + dp[i][j]) % MOD

                    # Left
                    if j == 0:
                        answer = (answer + dp[i][j]) % MOD
                    else:
                        new_dp[i][j - 1] = (new_dp[i][j - 1] + dp[i][j]) % MOD

                    # Right
                    if j == n - 1:
                        answer = (answer + dp[i][j]) % MOD
                    else:
                        new_dp[i][j + 1] = (new_dp[i][j + 1] + dp[i][j]) % MOD

            dp = new_dp

        return answer 