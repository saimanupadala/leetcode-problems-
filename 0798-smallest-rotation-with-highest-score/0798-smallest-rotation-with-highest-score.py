class Solution:
    def bestRotation(self, nums):
        n = len(nums)

        changes = [0] * (n + 1)

        for i, num in enumerate(nums):
            start = (i - num + 1) % n
            end = (i + 1) % n

            changes[start] -= 1
            changes[end] += 1

        score = sum(1 for i, num in enumerate(nums) if num <= i)

        max_score = score
        answer = 0

        for k in range(1, n):
            score += changes[k]

            if score > max_score:
                max_score = score
                answer = k

        return answer