
class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        island_id = 2
        area = {}

        def dfs(r, c, island_id):
            if (r < 0 or r >= n or c < 0 or c >= n
                    or grid[r][c] != 1):
                return 0

            grid[r][c] = island_id
            size = 1

            size += dfs(r + 1, c, island_id)
            size += dfs(r - 1, c, island_id)
            size += dfs(r, c + 1, island_id)
            size += dfs(r, c - 1, island_id)

            return size

        # Find each island and calculate its area
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # Largest island without changing any zero
        ans = max(area.values(), default=0)

        # Try changing each zero to one
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = set()

                    for dr, dc in [(1, 0), (-1, 0),
                                   (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < n and 0 <= nc < n:
                            if grid[nr][nc] > 1:
                                neighbors.add(grid[nr][nc])

                    total = 1
                    for island in neighbors:
                        total += area[island]

                    ans = max(ans, total)

        return ans
  