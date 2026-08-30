class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)
        F = 0
        for i in range(n):
            F += i * nums[i]
        ans = F
        for k in range(1, n):
            F = F + total - n * nums[n - k]
            ans = max(ans, F)

        return ans
        