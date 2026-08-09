from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        answer = 1
        for i in range(n):
            slopes = {}
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0:
                    slope = (1, 0)
                elif dy == 0:
                    slope = (0, 1)
                else:
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1
                answer = max(answer, slopes[slope] + 1)
        return answer
        