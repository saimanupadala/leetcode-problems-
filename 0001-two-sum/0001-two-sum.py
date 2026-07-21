class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in d:
                return [d[complement], i]

            d[nums[i]] = i
        