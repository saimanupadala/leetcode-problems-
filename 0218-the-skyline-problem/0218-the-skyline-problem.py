import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []

        # Create events
        for left, right, height in buildings:
            # Start event: negative height
            events.append((left, -height, right))

            # End event
            events.append((right, 0, 0))

        # Sort events by x-coordinate
        events.sort()

        result = []

        # Max heap: (-height, right)
        heap = [(0, float('inf'))]

        for x, neg_height, right in events:

            # Remove buildings that have ended
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Start a new building
            if neg_height != 0:
                heapq.heappush(heap, (neg_height, right))

            # Current maximum height
            current_height = -heap[0][0]

            # Add a key point only when height changes
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result