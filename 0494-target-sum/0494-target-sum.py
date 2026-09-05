class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}

        def dfs(index, total):
            if index == len(nums):
                return 1 if total == target else 0

            if (index, total) in memo:
                return memo[(index, total)]

            # Add +
            ways1 = dfs(index + 1, total + nums[index])

            # Add -
            ways2 = dfs(index + 1, total - nums[index])

            memo[(index, total)] = ways1 + ways2

            return memo[(index, total)]

        return dfs(0, 0)