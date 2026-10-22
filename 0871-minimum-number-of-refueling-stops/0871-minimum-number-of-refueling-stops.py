
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        fuel_heap = []
        fuel = startFuel
        stops = 0
        prev = 0

        for position, capacity in stations + [[target, 0]]:
            fuel -= position - prev

            while fuel < 0 and fuel_heap:
                fuel += -heapq.heappop(fuel_heap)
                stops += 1

            if fuel < 0:
                return -1

            heapq.heappush(fuel_heap, -capacity)
            prev = position

        return stops
