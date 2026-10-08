class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

    def get_size(self, i):
        return self.size[self.find(i)]


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        TOP = m * n
        uf = UnionFind(m * n + 1)

        # 1. Mark hit bricks in the grid
        for r, c in hits:
            if grid[r][c] == 1:
                grid[r][c] = 2

        def get_id(r, c):
            return r * n + c

        # 2. Build initial DSU state after all hits applied
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    idx = get_id(r, c)
                    if r == 0:
                        uf.union(idx, TOP)
                    if r > 0 and grid[r - 1][c] == 1:
                        uf.union(idx, get_id(r - 1, c))
                    if c > 0 and grid[r][c - 1] == 1:
                        uf.union(idx, get_id(r, c - 1))

        result = [0] * len(hits)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 3. Reconstruct grid in reverse order of hits
        for i in range(len(hits) - 1, -1, -1):
            r, c = hits[i]

            if grid[r][c] == 0:
                continue

            grid[r][c] = 1
            idx = get_id(r, c)
            prev_top_size = uf.get_size(TOP)

            is_connected_to_top = (r == 0)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    n_idx = get_id(nr, nc)
                    if uf.find(n_idx) == uf.find(TOP):
                        is_connected_to_top = True
                    uf.union(idx, n_idx)

            if r == 0:
                uf.union(idx, TOP)

            if is_connected_to_top:
                new_top_size = uf.get_size(TOP)
                result[i] = max(0, new_top_size - prev_top_size - 1)

        return result