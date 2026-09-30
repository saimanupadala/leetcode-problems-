class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))

        i = 1

        # Find where digits stop being increasing
        while i < len(digits) and digits[i - 1] <= digits[i]:
            i += 1

        if i == len(digits):
            return n

        # Move left and decrease the previous digit
        while i > 0 and digits[i - 1] > digits[i]:
            digits[i - 1] = str(int(digits[i - 1]) - 1)
            i -= 1

        # All digits after this position should be 9
        for j in range(i + 1, len(digits)):
            digits[j] = '9'

        return int(''.join(digits))