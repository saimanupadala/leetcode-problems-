import random

class Solution:

    def __init__(self, rects):
        self.rects = rects
        self.prefix = []

        total = 0

        for x1, y1, x2, y2 in rects:
        
            points = (x2 - x1 + 1) * (y2 - y1 + 1)

            total += points
            self.prefix.append(total)

        self.total = total

    def pick(self):
      
        k = random.randint(1, self.total)

       
        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix[mid] < k:
                left = mid + 1
            else:
                right = mid

        x1, y1, x2, y2 = self.rects[left]

        x = random.randint(x1, x2)
        y = random.randint(y1, y2)

        return [x, y]