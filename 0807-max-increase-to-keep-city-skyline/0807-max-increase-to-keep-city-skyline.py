class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Precompute the maximum height in each row and column
        max_row = [max(row) for row in grid]
        max_col = [max(grid[r][c] for r in range(n)) for c in range(n)]

        total_increase = 0

        # Calculate total height increase allowed for each building
        for r in range(n):
            for c in range(n):
                allowed_height = min(max_row[r], max_col[c])
                total_increase += allowed_height - grid[r][c]

        return total_increase