class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        for r in range(-n + 1, n):
            for c in range(-n + 1, n):
                count = 0

                for i in range(n):
                    for j in range(n):
                        x = i + r
                        y = j + c

                        if 0 <= x < n and 0 <= y < n:
                            if img1[i][j] == 1 and img2[x][y] == 1:
                                count += 1

                ans = max(ans, count)

        return ans