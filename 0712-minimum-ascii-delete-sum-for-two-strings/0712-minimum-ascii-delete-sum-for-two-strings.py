class Solution:
    def minimumDeleteSum(self, s1, s2):
        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Delete all characters from s1
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        # Delete all characters from s2
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    delete_s1 = ord(s1[i - 1]) + dp[i - 1][j]
                    delete_s2 = ord(s2[j - 1]) + dp[i][j - 1]

                    dp[i][j] = min(delete_s1, delete_s2)

        return dp[m][n]