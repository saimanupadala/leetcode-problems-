class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue if current number exceeds target
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                # Move to next index since each element is used once
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result
        