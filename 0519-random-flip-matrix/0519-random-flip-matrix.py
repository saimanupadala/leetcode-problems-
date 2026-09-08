import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.mp = {}

    def flip(self):
        # Pick a random position from remaining positions
        r = random.randrange(self.total)

        # Get the actual available position
        pos = self.mp.get(r, r)

        # One position is now used
        self.total -= 1

        # Replace the selected position with the last available position
        self.mp[r] = self.mp.get(self.total, self.total)

        # Convert 1D position to 2D coordinates
        return [pos // self.n, pos % self.n]

    def reset(self):
        self.total = self.m * self.n
        self.mp.clear()