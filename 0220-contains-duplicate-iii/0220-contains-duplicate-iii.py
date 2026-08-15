class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff < 0:
            return False

        buckets = {}

        # Bucket size
        size = valueDiff + 1

        def get_bucket(x):
            # Python's // handles negative values correctly
            return x // size

        for i, num in enumerate(nums):
            bucket = get_bucket(num)

            # Same bucket
            if bucket in buckets:
                return True

            # Check neighboring buckets
            if bucket - 1 in buckets:
                if abs(num - buckets[bucket - 1]) <= valueDiff:
                    return True

            if bucket + 1 in buckets:
                if abs(num - buckets[bucket + 1]) <= valueDiff:
                    return True

            # Add current number
            buckets[bucket] = num

            # Keep only the last indexDiff elements
            if i >= indexDiff:
                old_bucket = get_bucket(nums[i - indexDiff])
                del buckets[old_bucket]

        return False
        