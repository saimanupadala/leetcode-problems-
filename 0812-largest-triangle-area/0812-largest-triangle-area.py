from itertools import combinations
from typing import List


class Solution:

  def largestTriangleArea(self, points: List[List[int]]) -> float:
    max_area = 0.0

    # Iterate over all unique combinations of 3 points
    for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3):
      # Calculate triangle area using the Shoelace Formula
      area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
      max_area = max(max_area, area)

    return max_area