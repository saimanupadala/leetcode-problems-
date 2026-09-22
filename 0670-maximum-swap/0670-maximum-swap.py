class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        # Store the last position of each digit
        last = {}
        for i, digit in enumerate(digits):
            last[int(digit)] = i

        # Find the first digit that can be replaced
        for i in range(len(digits)):
            current = int(digits[i])

            # Try a larger digit from 9 down to current + 1
            for d in range(9, current, -1):
                if d in last and last[d] > i:
                    j = last[d]

                    # Swap
                    digits[i], digits[j] = digits[j], digits[i]

                    return int(''.join(digits))

        return num