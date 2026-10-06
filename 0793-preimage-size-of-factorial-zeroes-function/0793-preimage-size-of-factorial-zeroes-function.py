class Solution:
    def preimageSizeFZF(self, k):
        
        def trailingZeroes(x):
            count = 0
            
            while x > 0:
                x //= 5
                count += x
            
            return count

        # Find the first x where f(x) >= k
        left = 0
        right = 5 * (k + 1)

        while left < right:
            mid = (left + right) // 2

            if trailingZeroes(mid) < k:
                left = mid + 1
            else:
                right = mid

        # Check whether f(x) is exactly k
        if trailingZeroes(left) == k:
            return 5

        return 0