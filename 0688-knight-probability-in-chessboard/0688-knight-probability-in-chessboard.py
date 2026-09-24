class Solution:
    def knightProbability(self, n, k, row, column):
        moves = [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2)
        ]

        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1.0

        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]

            for r in range(n):
                for c in range(n):
                    if dp[r][c] == 0:
                        continue

                    for dr, dc in moves:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += dp[r][c] / 8

            dp = new_dp

        return sum(map(sum, dp))