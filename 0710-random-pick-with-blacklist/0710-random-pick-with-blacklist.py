import random

class Solution:

    def __init__(self, n, blacklist):
        self.m = n - len(blacklist)
        self.mapping = {}

        black = set(blacklist)

        last = n - 1

        for b in blacklist:
            if b < self.m:
                while last in black:
                    last -= 1

                self.mapping[b] = last
                last -= 1

    def pick(self):
        x = random.randrange(self.m)

        if x in self.mapping:
            return self.mapping[x]

        return x