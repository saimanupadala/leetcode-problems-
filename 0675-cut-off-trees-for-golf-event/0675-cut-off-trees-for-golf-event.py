from collections import deque

class Solution:
    def cutOffTree(self, forest):
        m = len(forest)
        n = len(forest[0])

        # Get all trees and sort by height
        trees = []

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))

        trees.sort()

        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0

            queue = deque([(sr, sc, 0)])
            visited = {(sr, sc)}

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                r, c, steps = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        forest[nr][nc] != 0 and
                        (nr, nc) not in visited):

                        if nr == tr and nc == tc:
                            return steps + 1

                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))

            return -1

        total = 0
        current_r = 0
        current_c = 0

        # Visit trees from shortest to tallest
        for height, r, c in trees:
            distance = bfs(current_r, current_c, r, c)

            if distance == -1:
                return -1

            total += distance

            current_r = r
            current_c = c

            # Tree becomes an empty cell after cutting
            forest[r][c] = 1

        return total