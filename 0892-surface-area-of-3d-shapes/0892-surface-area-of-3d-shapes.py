
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]

                if h > 0:
                    result += 2
                    result += 4 * h

                    if i > 0:
                        result -= 2 * min(h, grid[i-1][j])

                    if j > 0:
                        result -= 2 * min(h, grid[i][j-1])

        return result
