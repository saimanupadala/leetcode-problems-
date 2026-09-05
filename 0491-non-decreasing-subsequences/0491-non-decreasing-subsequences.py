class Solution:
    def findSubsequences(self, nums):
        result = []
        path = []

        def backtrack(start):
            # A valid subsequence must have at least 2 elements
            if len(path) >= 2:
                result.append(path.copy())

            used = set()  # Avoid duplicates at this recursion level

            for i in range(start, len(nums)):
                # Skip duplicate choices at the same level
                if nums[i] in used:
                    continue

                # Must be non-decreasing
                if path and nums[i] < path[-1]:
                    continue

                used.add(nums[i])
                path.append(nums[i])

                backtrack(i + 1)

                path.pop()

        backtrack(0)
        return result