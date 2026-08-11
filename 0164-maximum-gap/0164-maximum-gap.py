class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0
        gap = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // gap + 1
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count
        used = [False] * bucket_count
        for num in nums:
            index = (num - min_val) // gap
            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
            used[index] = True
        maximum_gap = 0
        previous_max = min_val
        for i in range(bucket_count):
            if not used[i]:
                continue
            maximum_gap = max(maximum_gap, bucket_min[i] - previous_max)
            previous_max = bucket_max[i]
        return maximum_gap
        