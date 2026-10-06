class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):

        def count(limit):
            ans = 0
            length = 0

            for num in nums:
                if num <= limit:
                    length += 1
                    ans += length
                else:
                    length = 0

            return ans

        return count(right) - count(left - 1)  