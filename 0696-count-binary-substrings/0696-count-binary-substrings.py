class Solution:
    def countBinarySubstrings(self, s):
        prev = 0
        curr = 1
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev = curr
                curr = 1

        # Count the last pair of groups
        ans += min(prev, curr)

        return ans