class Solution:
    def findMaxLength(self, nums):
        # prefix_sum -> first index
        mp = {0: -1}

        prefix = 0
        max_len = 0

        for i, num in enumerate(nums):

            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in mp:
                # Equal number of 0s and 1s
                max_len = max(max_len, i - mp[prefix])
            else:
                # Store only the first occurrence
                mp[prefix] = i

        return max_len