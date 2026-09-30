class Solution:
    def cherryPickup(self, grid):
        n = len(grid)

        # dp[r1][r2] = maximum cherries collected
        # when person 1 is at (r1, c1)
        # and person 2 is at (r2, c2)
        dp = [[-1] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for k in range(1, 2 * n - 1):
            new_dp = [[-1] * n for _ in range(n)]

            for r1 in range(n):
                c1 = k - r1

                if c1 < 0 or c1 >= n:
                    continue

                for r2 in range(n):
                    c2 = k - r2

                    if c2 < 0 or c2 >= n:
                        continue

                    # Thorn cell
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    best = -1

                    # Both move down
                    if r1 > 0 and r2 > 0:
                        best = max(best, dp[r1 - 1][r2 - 1])

                    # Person 1 down, Person 2 right
                    if r1 > 0:
                        best = max(best, dp[r1 - 1][r2])

                    # Person 1 right, Person 2 down
                    if r2 > 0:
                        best = max(best, dp[r1][r2 - 1])

                    # Both move right
                    best = max(best, dp[r1][r2])

                    if best == -1:
                        continue

                    cherries = grid[r1][c1]

                    # Don't count the same cell twice
                    if r1 != r2:
                        cherries += grid[r2][c2]

                    new_dp[r1][r2] = best + cherries

            dp = new_dp

        return max(0, dp[n - 1][n - 1])