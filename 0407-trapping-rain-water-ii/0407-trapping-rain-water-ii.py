import heapq

class Solution:
    def trapRainWater(self, heightMap):

        m = len(heightMap)
        n = len(heightMap[0])

      
        if m <= 2 or n <= 2:
            return 0

        heap = []
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))

            visited[i][0] = True
            visited[i][n - 1] = True

        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))

            visited[0][j] = True
            visited[m - 1][j] = True

        water = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while heap:

            height, row, col = heapq.heappop(heap)

            for dr, dc in directions:

                nr = row + dr
                nc = col + dc

            
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:

                    visited[nr][nc] = True

               
                    if height > heightMap[nr][nc]:
                        water += height - heightMap[nr][nc]

               
                    new_height = max(height, heightMap[nr][nc])

                    heapq.heappush(heap, (new_height, nr, nc))

        return water
        