class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        # Total must be divisible by k
        if total % k != 0:
            return False

        target = total // k

        # If any number is bigger than target, impossible
        if max(nums) > target:
            return False

        nums.sort(reverse=True)

        n = len(nums)
        used = [False] * n

        def backtrack(start, groups, current_sum):
            # All k groups are successfully formed
            if groups == k - 1:
                return True

            # Current group is complete
            if current_sum == target:
                return backtrack(0, groups + 1, 0)

            for i in range(start, n):
                if used[i]:
                    continue

                # Don't exceed target
                if current_sum + nums[i] > target:
                    continue

                used[i] = True

                if backtrack(i + 1, groups, current_sum + nums[i]):
                    return True

                used[i] = False

                # Avoid trying the same value again
                if current_sum == 0:
                    break

            return False

        return backtrack(0, 0, 0)