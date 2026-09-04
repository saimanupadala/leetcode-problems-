class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        ans = 0

        # Check every bit position
        for bit in range(31):
            ones = 0

            # Count numbers having 1 at this bit
            for num in nums:
                if num & (1 << bit):
                    ones += 1

            zeros = len(nums) - ones

            # Every 1 can form a different pair with every 0
            ans += ones * zeros

        return ans