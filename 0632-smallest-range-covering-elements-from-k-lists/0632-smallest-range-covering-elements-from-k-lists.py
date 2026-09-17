import heapq

class Solution:
    def smallestRange(self, nums):
        heap = []
        current_max = float('-inf')

        # Put the first element of every list into the heap
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        best_left = heap[0][0]
        best_right = current_max

        while True:
            current_min, list_index, element_index = heapq.heappop(heap)

            # Check current range
            if current_max - current_min < best_right - best_left:
                best_left = current_min
                best_right = current_max

            # Move to the next element in this list
            if element_index + 1 == len(nums[list_index]):
                break

            next_value = nums[list_index][element_index + 1]
            heapq.heappush(
                heap,
                (next_value, list_index, element_index + 1)
            )

            current_max = max(current_max, next_value)

        return [best_left, best_right]