class Solution:
    def isIdealPermutation(self, nums):
        max_value = 0

        for i in range(len(nums)):
            if i >= 2:
                max_value = max(max_value, nums[i - 2])

                if max_value > nums[i]:
                    return False

        return True