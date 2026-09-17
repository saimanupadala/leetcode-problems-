class Solution:
    def findMaxAverage(self, nums, k):
        # Sum of first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k