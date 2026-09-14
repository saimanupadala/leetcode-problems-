class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        # Find first different position
        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1

        # Already sorted
        if left == len(nums):
            return 0

        # Find last different position
        while nums[right] == sorted_nums[right]:
            right -= 1

        return right - left + 1   