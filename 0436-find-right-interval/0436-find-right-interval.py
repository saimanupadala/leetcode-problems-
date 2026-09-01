class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)

        # Store (start, original_index)
        starts = []

        for i in range(n):
            starts.append((intervals[i][0], i))

        # Sort by start time
        starts.sort()

        result = [-1] * n

        for i in range(n):
            end = intervals[i][1]

            # Binary search for smallest start >= end
            left = 0
            right = n - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if starts[mid][0] >= end:
                    ans = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1

            result[i] = ans

        return result
        