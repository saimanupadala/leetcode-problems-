class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        # dp[j] = largest square ending at current row, column j
        dp = [0] * (n + 1)

        max_side = 0

        for i in range(1, m + 1):
            prev = 0  # dp[j-1] from the previous row

            for j in range(1, n + 1):
                temp = dp[j]

                if matrix[i - 1][j - 1] == "1":
                    dp[j] = 1 + min(
                        dp[j],      # top
                        dp[j - 1],  # left
                        prev        # top-left
                    )

                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0

                prev = temp

        return max_side * max_side
        