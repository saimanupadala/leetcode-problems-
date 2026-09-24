class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)

        # Calculate sum of every subarray of length k
        sums = [0] * (n - k + 1)

        window = sum(nums[:k])
        sums[0] = window

        for i in range(k, n):
            window += nums[i] - nums[i - k]
            sums[i - k + 1] = window

        # best_left[i] = index of maximum sum from 0 to i
        best_left = [0] * len(sums)
        best = 0

        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            best_left[i] = best

        # best_right[i] = index of maximum sum from i to end
        # Use >= so that the smaller index is chosen in a tie
        best_right = [0] * len(sums)
        best = len(sums) - 1

        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            best_right[i] = best

        # Try every possible middle subarray
        max_total = 0
        answer = []

        for mid in range(k, len(sums) - k):
            left = best_left[mid - k]
            right = best_right[mid + k]

            total = sums[left] + sums[mid] + sums[right]

            if total > max_total:
                max_total = total
                answer = [left, mid, right]

        return answer