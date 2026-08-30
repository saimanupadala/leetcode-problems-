import random

class Solution:

    def __init__(self, nums):
        self.indices = {}

        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []

            self.indices[num].append(i)

    def pick(self, target):
        return random.choice(self.indices[target])