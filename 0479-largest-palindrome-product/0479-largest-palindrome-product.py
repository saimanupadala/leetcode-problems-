class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10 ** n - 1
        lower = 10 ** (n - 1)

        for left in range(upper, lower - 1, -1):
            # Create palindrome from left half
            s = str(left)
            pal = int(s + s[::-1])

            # Check whether palindrome can be made
            # by multiplying two n-digit numbers
            x = upper

            while x * x >= pal:
                if pal % x == 0:
                    other = pal // x

                    if lower <= other <= upper:
                        return pal % 1337

                x -= 1

        return 0
        