class Solution:
    def findIntegers(self, n):
        # dp[i] = number of binary strings of length i
        # that do not contain consecutive 1s
        dp = [0] * 32

        dp[0] = 1
        dp[1] = 2

        for i in range(2, 32):
            dp[i] = dp[i - 1] + dp[i - 2]

        ans = 0
        prev_bit = 0

        # Check bits from left to right
        for i in range(30, -1, -1):
            if n & (1 << i):
                ans += dp[i]

                # Two consecutive 1s
                if prev_bit == 1:
                    return ans

                prev_bit = 1
            else:
                prev_bit = 0

        # Include n itself
        return ans + 1
    