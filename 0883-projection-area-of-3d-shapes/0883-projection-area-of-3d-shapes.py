
class Solution:
    def projectionArea(self, grid):
        top = 0
        front = 0
        side = 0

        n = len(grid)

        for i in range(n):
            front += max(grid[i])

            for j in range(n):
                if grid[i][j] > 0:
                    top += 1

        for j in range(n):
            side += max(grid[i][j] for i in range(n))

        return top + front + side
