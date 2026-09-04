import random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> list[float]:
        while True:
            # Generate a random point inside the bounding square
            x = random.uniform(-self.radius, self.radius)
            y = random.uniform(-self.radius, self.radius)

            # Check if point is inside the circle
            if x * x + y * y <= self.radius * self.radius:
                return [
                    self.x_center + x,
                    self.y_center + y
                ]