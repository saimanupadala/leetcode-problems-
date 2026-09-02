class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1

        pigs = 0
        combinations = 1

        while combinations < buckets:
            combinations *= states
            pigs += 1

        return pigs