class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        score = 0

        for j in range(n):
            ones = sum(grid[i][j] for i in range(m))
            ones = max(ones, m - ones)
            score += ones * (1 << (n - j - 1))

        return score 