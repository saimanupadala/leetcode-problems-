class Solution:
    def rotatedDigits(self, n):
        count = 0

        for num in range(1, n + 1):
            x = num
            changed = False
            valid = True

            while x > 0:
                digit = x % 10

                if digit in [3, 4, 7]:
                    valid = False
                    break

                if digit in [2, 5, 6, 9]:
                    changed = True

                x //= 10

            if valid and changed:
                count += 1

        return count