class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2

            count = 0
            row = n - 1
            col = 0

            # Count numbers <= mid
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
        