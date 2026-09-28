import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]