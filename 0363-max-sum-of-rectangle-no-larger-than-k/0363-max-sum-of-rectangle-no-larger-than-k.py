from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])
        if m < n:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m
        answer = float('-inf')
        for top in range(m):
            col_sum = [0] * n

            for bottom in range(top, m):
      
                for col in range(n):
                    col_sum[col] += matrix[bottom][col]
                prefix = 0
                sorted_prefix = [0]

                for value in col_sum:
                    prefix += value
                    pos = bisect_left(sorted_prefix, prefix - k)
                    if pos < len(sorted_prefix):
                        answer = max(
                            answer,
                            prefix - sorted_prefix[pos]
                        )

                    insort(sorted_prefix, prefix)
                    if answer == k:
                        return k

        return answer
        