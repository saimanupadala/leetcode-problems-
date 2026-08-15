class Solution:
    def combinationSum3(self, k, n):
        result = []
        def backtrack(start, path, remaining):
            if len(path) == k:
                if remaining == 0:
                    result.append(path[:])
                return
            for num in range(start, 10):
                if num > remaining:
                    break
                path.append(num)
                backtrack(num + 1, path, remaining - num)
                path.pop()
        backtrack(1, [], n)

        return result
        