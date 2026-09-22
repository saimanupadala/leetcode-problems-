class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low = 1
        high = m * n

        while low < high:
            mid = (low + high) // 2

            # Count numbers <= mid
            count = 0
            for i in range(1, m + 1):
                count += min(n, mid // i)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low