class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))

        # Step 1: Find the first decreasing digit from the right
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        # No greater permutation exists
        if i < 0:
            return -1

        # Step 2: Find the smallest digit greater than digits[i]
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse everything after i
        digits[i + 1:] = reversed(digits[i + 1:])

        result = int("".join(digits))

        # Check 32-bit signed integer limit
        if result > 2**31 - 1:
            return -1

        return result 