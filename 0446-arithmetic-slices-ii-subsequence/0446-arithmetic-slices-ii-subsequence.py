class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)

        dp = [dict() for _ in range(n)]

        answer = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

            
                count = dp[j].get(diff, 0)

                dp[i][diff] = dp[i].get(diff, 0) + count + 1

                answer += count

        return answer