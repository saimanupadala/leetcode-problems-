class Solution:
    def maxEnvelopes(self, envelopes):
        # Sort width increasing
        # For same width, height decreasing
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Find LIS of heights
        heights = []
        
        for w, h in envelopes:
            left = 0
            right = len(heights)

            while left < right:
                mid = (left + right) // 2

                if heights[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            if left == len(heights):
                heights.append(h)
            else:
                heights[left] = h

        return len(heights)
        
        