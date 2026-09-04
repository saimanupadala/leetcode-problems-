class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)

        # dp[i][j] = maximum score difference
        # current player can achieve from nums[i...j]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                take_left = nums[i] - dp[i + 1][j]
                take_right = nums[j] - dp[i][j - 1]

                dp[i][j] = max(take_left, take_right)

        return dp[0][n - 1] >= 0