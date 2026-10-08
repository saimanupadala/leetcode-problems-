class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        total_sum = sum(nums)
        
        # dp[k] will hold all possible sums using exactly k elements
        dp = [set() for _ in range(n // 2 + 1)]
        dp[0].add(0)

        for num in nums:
            # Update dp backwards to avoid using the same element multiple times
            for k in range(n // 2, 0, -1):
                for prev_sum in dp[k - 1]:
                    dp[k].add(prev_sum + num)

        # Check if any valid size k satisfies (k * total_sum) % n == 0
        for k in range(1, n // 2 + 1):
            if (total_sum * k) % n == 0:
                target_sum = (total_sum * k) // n
                if target_sum in dp[k]:
                    return True

        return False   