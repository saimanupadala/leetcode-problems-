class Solution:
    def validSquare(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]

        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        distances = []

        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(dist(points[i], points[j]))

        distances.sort()

        # 4 equal sides, 2 equal diagonals
        # Side must have positive length
        return (
            distances[0] > 0 and
            distances[0] == distances[1] == distances[2] == distances[3] and
            distances[4] == distances[5] and
            distances[4] == 2 * distances[0]
        )

