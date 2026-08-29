class Solution:
    def lastRemaining(self, n):
        head = 1
        step = 1
        remaining = n
        left = True

        while remaining > 1:

            # Head changes if:
            # 1. We eliminate from left
            # 2. We eliminate from right and number of elements is odd
            if left or remaining % 2 == 1:
                head += step

            # After every round:
            remaining //= 2
            step *= 2

            # Change direction
            left = not left

        return head
        