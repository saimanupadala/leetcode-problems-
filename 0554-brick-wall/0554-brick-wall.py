class Solution:
    def leastBricks(self, wall):
        edges = {}

        for row in wall:
            position = 0

            # Don't include the last edge of each row
            for brick in row[:-1]:
                position += brick
                edges[position] = edges.get(position, 0) + 1

        max_edges = max(edges.values(), default=0)

        return len(wall) - max_edges