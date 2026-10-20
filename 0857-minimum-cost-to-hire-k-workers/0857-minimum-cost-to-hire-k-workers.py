import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted(
            (w / q, q) for q, w in zip(quality, wage)
        )

        max_heap = []
        total_quality = 0
        ans = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)

            if len(max_heap) == k:
                ans = min(ans, ratio * total_quality)

        return ans