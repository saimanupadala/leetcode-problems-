class Solution:
    def arrayNesting(self, nums):
        n = len(nums)
        visited = [False] * n
        longest = 0

        for i in range(n):
            if not visited[i]:
                count = 0
                j = i

                while not visited[j]:
                    visited[j] = True
                    j = nums[j]
                    count += 1

                longest = max(longest, count)

        return longest