import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        pq = [(grid[0][0], 0, 0)]
        visited = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            time, r, c = heapq.heappop(pq)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Reached bottom-right
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(pq, (new_time, nr, nc))