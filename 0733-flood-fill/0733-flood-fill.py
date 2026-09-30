class Solution:
    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]

        if old_color == color:
            return image

        def dfs(r, c):
            # Change current pixel
            image[r][c] = color

            # Four directions
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check valid position and same original color
                if (0 <= nr < len(image) and
                    0 <= nc < len(image[0]) and
                    image[nr][nc] == old_color):

                    dfs(nr, nc)

        dfs(sr, sc)

        return image