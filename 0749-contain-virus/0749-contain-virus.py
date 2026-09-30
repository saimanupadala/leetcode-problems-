class Solution:
    def containVirus(self, isInfected):
        m = len(isInfected)
        n = len(isInfected[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total_walls = 0

        while True:
            regions = []
            frontiers = []
            walls = []

            visited = [[False] * n for _ in range(m)]

            # Find all infected regions
            for i in range(m):
                for j in range(n):

                    if isInfected[i][j] == 1 and not visited[i][j]:

                        region = []
                        frontier = set()
                        wall_count = 0

                        stack = [(i, j)]
                        visited[i][j] = True

                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))

                            for dx, dy in directions:
                                nx = x + dx
                                ny = y + dy

                                if 0 <= nx < m and 0 <= ny < n:

                                    if isInfected[nx][ny] == 1:
                                        if not visited[nx][ny]:
                                            visited[nx][ny] = True
                                            stack.append((nx, ny))

                                    elif isInfected[nx][ny] == 0:
                                        frontier.add((nx, ny))
                                        wall_count += 1

                        regions.append(region)
                        frontiers.append(frontier)
                        walls.append(wall_count)

            # No region can spread
            if not regions:
                break

            # Find region threatening the most cells
            best = 0

            for i in range(1, len(regions)):
                if len(frontiers[i]) > len(frontiers[best]):
                    best = i

            # Build walls around the selected region
            total_walls += walls[best]

            # Mark selected region as quarantined
            for x, y in regions[best]:
                isInfected[x][y] = 2

            # Spread all other regions
            for i in range(len(regions)):
                if i == best:
                    continue

                for x, y in frontiers[i]:
                    isInfected[x][y] = 1

        return total_walls