import random
import bisect

class Solution:

    def __init__(self, w):
        self.prefix = []
        
        total = 0
        
        for weight in w:
            total += weight
            self.prefix.append(total)
        
        self.total = total

    def pickIndex(self):
        # Pick a random number from 1 to total
        target = random.randint(1, self.total)
        
        # Find the first prefix sum >= target
        return bisect.bisect_left(self.prefix, target)