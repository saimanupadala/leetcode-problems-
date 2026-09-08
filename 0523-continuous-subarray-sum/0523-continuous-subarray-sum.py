class Solution:
    def checkSubarraySum(self, nums, k):
        # remainder -> first index
        remainder = {0: -1}

        total = 0

        for i, num in enumerate(nums):
            total += num
            rem = total % k

            if rem in remainder:
                # Make sure subarray length is at least 2
                if i - remainder[rem] >= 2:
                    return True
            else:
                # Store only the first occurrence
                remainder[rem] = i

        return False