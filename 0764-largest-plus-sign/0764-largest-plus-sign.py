class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: list[list[int]]) -> int:
        grid = [[1] * n for _ in range(n)]

        for r, c in mines:
            grid[r][c] = 0

        # dp stores the minimum arm length found so far
        dp = [[0] * n for _ in range(n)]

        # Left
        for r in range(n):
            count = 0
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1
                else:
                    count = 0
                dp[r][c] = count

        # Right
        for r in range(n):
            count = 0
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    count += 1
                    dp[r][c] = min(dp[r][c], count)
                else:
                    count = 0

        # Up
        for c in range(n):
            count = 0
            for r in range(n):
                if grid[r][c] == 1:
                    count += 1
                    dp[r][c] = min(dp[r][c], count)
                else:
                    count = 0

        # Down + answer
        ans = 0

        for c in range(n):
            count = 0
            for r in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    count += 1
                    dp[r][c] = min(dp[r][c], count)
                    ans = max(ans, dp[r][c])
                else:
                    count = 0

        return ans