class Solution:
    def maxChunksToSorted(self, arr):
        sorted_arr = sorted(arr)

        chunks = 0
        max_value = 0

        for i in range(len(arr)):
            max_value = max(max_value, arr[i])

            if max_value == sorted_arr[i]:
                chunks += 1

        return chunks