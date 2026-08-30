class Solution:
    def pacificAtlantic(self, heights):

        m = len(heights)
        n = len(heights[0])

        def dfs(r, c, visited):

            visited.add((r, c))

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):

                    dfs(nr, nc, visited)

        pacific = set()
        atlantic = set()

        for c in range(n):
            dfs(0, c, pacific)

        for r in range(m):
            dfs(r, 0, pacific)

        for c in range(n):
            dfs(m - 1, c, atlantic)

        for r in range(m):
            dfs(r, n - 1, atlantic)

   
        result = []

        for r in range(m):
            for c in range(n):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
        