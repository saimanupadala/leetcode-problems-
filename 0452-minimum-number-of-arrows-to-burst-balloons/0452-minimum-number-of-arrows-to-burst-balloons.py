class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # Sort balloons by their ending point
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_position = points[0][1]

        for start, end in points[1:]:
            # Current balloon is not burst by the previous arrow
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows