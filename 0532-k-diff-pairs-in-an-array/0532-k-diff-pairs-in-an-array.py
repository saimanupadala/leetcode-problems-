class Solution:
    def findPairs(self, nums, k):
        if k == 0:
            count = {}
            for num in nums:
                count[num] = count.get(num, 0) + 1

            return sum(1 for value in count.values() if value >= 2)

        nums_set = set(nums)
        count = 0

        for num in nums_set:
            if num + k in nums_set:
                count += 1

        return count  