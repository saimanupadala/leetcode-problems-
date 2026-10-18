
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        last_person = -1

        for i in range(len(seats)):
            if seats[i] == 1:
                if last_person == -1:
                    max_distance = i
                else:
                    max_distance = max(
                        max_distance, (i - last_person) // 2
                    )
                last_person = i

        max_distance = max(max_distance, len(seats) - 1 - last_person)

        return max_distance
