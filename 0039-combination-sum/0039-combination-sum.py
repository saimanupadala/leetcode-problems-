class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Reuse the same element
                backtrack(i, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result
        