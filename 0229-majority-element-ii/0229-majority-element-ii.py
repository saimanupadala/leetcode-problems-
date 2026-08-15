class Solution:
    def majorityElement(self, nums):
        # There can be at most 2 elements
        # appearing more than n/3 times.
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        # First pass: find candidates
        for num in nums:
            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Second pass: verify candidates
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        result = []
        n = len(nums)

        if count1 > n // 3:
            result.append(candidate1)

        if count2 > n // 3:
            result.append(candidate2)

        return result
        