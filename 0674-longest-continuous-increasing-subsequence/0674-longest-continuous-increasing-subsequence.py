class Solution:
    def findLengthOfLCIS(self, nums):
        current = 1
        longest = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                current = 1

            longest = max(longest, current)

        return longest