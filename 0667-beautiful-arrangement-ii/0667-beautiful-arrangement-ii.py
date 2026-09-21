class Solution:
    def constructArray(self, n, k):
        answer = []

        left = 1
        right = k + 1

        # Create k different differences
        while left <= right:
            if len(answer) % 2 == 0:
                answer.append(left)
                left += 1
            else:
                answer.append(right)
                right -= 1

        # Add remaining numbers
        for num in range(k + 2, n + 1):
            answer.append(num)

        return answer