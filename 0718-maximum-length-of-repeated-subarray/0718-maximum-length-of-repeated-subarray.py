class Solution:
    def findLength(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                    ans = max(ans, dp[i][j])

        return ans