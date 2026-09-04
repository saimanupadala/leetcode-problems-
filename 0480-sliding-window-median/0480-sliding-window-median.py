import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:

        small = []   # max heap
        large = []   # min heap
        delayed = defaultdict(int)

        small_size = 0
        large_size = 0

        def prune_small():
            while small and delayed[-small[0]] > 0:
                delayed[-small[0]] -= 1
                heapq.heappop(small)

        def prune_large():
            while large and delayed[large[0]] > 0:
                delayed[large[0]] -= 1
                heapq.heappop(large)

        def balance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                x = -heapq.heappop(small)
                heapq.heappush(large, x)

                small_size -= 1
                large_size += 1

                prune_small()

            elif small_size < large_size:
                x = heapq.heappop(large)
                heapq.heappush(small, -x)

                large_size -= 1
                small_size += 1

                prune_large()

        # Build first window
        for i in range(k):
            if not small or nums[i] <= -small[0]:
                heapq.heappush(small, -nums[i])
                small_size += 1
            else:
                heapq.heappush(large, nums[i])
                large_size += 1

            # IMPORTANT: balance after every insertion
            balance()

        result = []

        # First median
        if k % 2 == 1:
            result.append(float(-small[0]))
        else:
            result.append((-small[0] + large[0]) / 2.0)

        # Slide the window
        for i in range(k, len(nums)):

            incoming = nums[i]
            outgoing = nums[i - k]

            # Add incoming number
            if incoming <= -small[0]:
                heapq.heappush(small, -incoming)
                small_size += 1
            else:
                heapq.heappush(large, incoming)
                large_size += 1

            # Mark outgoing number for deletion
            delayed[outgoing] += 1

            if outgoing <= -small[0]:
                small_size -= 1
            else:
                large_size -= 1

            # Remove invalid top elements
            prune_small()
            prune_large()

            # Balance
            balance()

            # Get median
            if k % 2 == 1:
                result.append(float(-small[0]))
            else:
                result.append((-small[0] + large[0]) / 2.0)

        return result