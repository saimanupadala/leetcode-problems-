class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen:
                if i - last_seen[num] <= k:
                    return True

            last_seen[num] = i

        return False
        