import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        heap = []

        # Put the smallest fraction from each numerator
        for i in range(n - 1):
            heapq.heappush(heap, (arr[i] / arr[n - 1], i, n - 1))

        # Remove the smallest fraction k-1 times
        for _ in range(k - 1):
            value, i, j = heapq.heappop(heap)

            if j - 1 > i:
                heapq.heappush(
                    heap,
                    (arr[i] / arr[j - 1], i, j - 1)
                )

        value, i, j = heapq.heappop(heap)

        return [arr[i], arr[j]]