class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        heaters.sort()

        answer = 0

        for house in houses:
            # Find the position where house would be inserted
            left = 0
            right = len(heaters)

            while left < right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid

            # left is the first heater >= house
            dist_right = float('inf')
            dist_left = float('inf')

            if left < len(heaters):
                dist_right = heaters[left] - house

            if left > 0:
                dist_left = house - heaters[left - 1]

            # Nearest heater distance
            nearest = min(dist_left, dist_right)

            answer = max(answer, nearest)

        return answer