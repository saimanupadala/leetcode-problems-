class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)

        # length[i] = length of LIS ending at i
        # count[i] = number of LIS of that length ending at i
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:

                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]

                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        longest = max(length)

        answer = 0
        for i in range(n):
            if length[i] == longest:
                answer += count[i]

        return answer