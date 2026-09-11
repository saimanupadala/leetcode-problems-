class Solution:
    def checkRecord(self, n):
        MOD = 10**9 + 7

        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            new = [[0] * 3 for _ in range(2)]

            for a in range(2):
                for l in range(3):
                    val = dp[a][l]

                    if val == 0:
                        continue

                    # Present
                    new[a][0] = (new[a][0] + val) % MOD

                    # Late
                    if l < 2:
                        new[a][l + 1] = (new[a][l + 1] + val) % MOD

                    # Absent
                    if a < 1:
                        new[a + 1][0] = (new[a + 1][0] + val) % MOD

            dp = new

        ans = 0
        for a in range(2):
            for l in range(3):
                ans = (ans + dp[a][l]) % MOD

        return ans    