class Solution:
    def fallingSquares(self, positions):
        ans = []
        intervals = []   # [left, right, height]
        max_height = 0

        for left, side in positions:
            right = left + side
            height = side

            # Check all previously dropped squares
            for l, r, h in intervals:

                # Overlap condition
                if left < r and right > l:
                    height = max(height, h + side)

            # Store this square
            intervals.append((left, right, height))

            # Update tallest height
            max_height = max(max_height, height)
            ans.append(max_height)

        return ans