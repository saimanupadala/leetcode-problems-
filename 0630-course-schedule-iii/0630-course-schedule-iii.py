import heapq

class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])

        total = 0
        max_heap = []

        for duration, lastDay in courses:
            total += duration
            heapq.heappush(max_heap, -duration)

            if total > lastDay:
                longest = -heapq.heappop(max_heap)
                total -= longest

        return len(max_heap)