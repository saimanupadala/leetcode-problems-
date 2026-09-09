class Solution:
    def removeBoxes(self, boxes):
        
        from functools import lru_cache

        @lru_cache(None)
        def dp(left, right, k):
            if left > right:
                return 0

            # Combine boxes of the same color
            while left < right and boxes[left] == boxes[left + 1]:
                left += 1
                k += 1

            # Option 1: Remove the current group now
            ans = (k + 1) * (k + 1) + dp(left + 1, right, 0)

            # Option 2: Keep it and combine with
            # another box of the same color later
            for i in range(left + 1, right + 1):
                if boxes[i] == boxes[left]:
                    ans = max(
                        ans,
                        dp(left + 1, i - 1, 0) +
                        dp(i, right, k + 1)
                    )

            return ans

        return dp(0, len(boxes) - 1, 0)