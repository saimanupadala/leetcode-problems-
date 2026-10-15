
class Solution:
    def numMagicSquaresInside(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                nums = [grid[i + x][j + y]
                        for x in range(3)
                        for y in range(3)]

                if sorted(nums) != list(range(1, 10)):
                    continue

                if grid[i + 1][j + 1] != 5:
                    continue

                magic = True

                for x in range(3):
                    if sum(grid[i + x][j:j + 3]) != 15:
                        magic = False

                for y in range(3):
                    if sum(grid[i + x][j + y]
                           for x in range(3)) != 15:
                        magic = False

                if sum(grid[i + x][j + x]
                       for x in range(3)) != 15:
                    magic = False

                if sum(grid[i + x][j + 2 - x]
                       for x in range(3)) != 15:
                    magic = False

                if magic:
                    count += 1

        return count
