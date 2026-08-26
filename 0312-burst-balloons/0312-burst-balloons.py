class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]


        for length in range(2, n):
            for left in range(n - length):
                right = left + length

            
                for k in range(left + 1, right):
                    coins = (
                        nums[left] * nums[k] * nums[right]
                        + dp[left][k]
                        + dp[k][right]
                    )

                    dp[left][right] = max(
                        dp[left][right],
                        coins
                    )

        return dp[0][n - 1]