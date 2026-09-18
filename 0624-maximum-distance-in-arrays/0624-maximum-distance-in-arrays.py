class Solution:
    def maxDistance(self, arrays):
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):
            # Compare current array with previous arrays
            ans = max(
                ans,
                abs(arrays[i][-1] - min_val),
                abs(max_val - arrays[i][0])
            )

            # Update global minimum and maximum
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return ans