class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by ending time
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            # Overlap found
            if intervals[i][0] < prev_end:
                count += 1
            else:
                # No overlap
                prev_end = intervals[i][1]

        return count
        