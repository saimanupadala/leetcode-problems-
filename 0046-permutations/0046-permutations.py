class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path)
                return

            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return result
        