class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        result = 10
        unique = 9
        available = 9
        for digits in range(2, n + 1):
            unique *= available
            result += unique
            available -= 1
        return result
        