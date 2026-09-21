class Solution:
    def checkPossibility(self, nums):
        count = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1

                if count > 1:
                    return False

                # Modify the larger element
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]

        return True