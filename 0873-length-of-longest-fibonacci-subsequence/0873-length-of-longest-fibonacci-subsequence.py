
class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = [[2] * n for _ in range(n)]
        ans = 0

        for j in range(n):
            for i in range(j):
                prev = arr[j] - arr[i]

                if prev < arr[i] and prev in index:
                    k = index[prev]
                    dp[i][j] = dp[k][i] + 1
                    ans = max(ans, dp[i][j])

        return ans if ans >= 3 else 0
 