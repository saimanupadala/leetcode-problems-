class Solution:
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                # Check 3 x 3 surrounding cells
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni = i + di
                        nj = j + dj

                        # Check if cell is inside the image
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1

                res[i][j] = total // count

        return res