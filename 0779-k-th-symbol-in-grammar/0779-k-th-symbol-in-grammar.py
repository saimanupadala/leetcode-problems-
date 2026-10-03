class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # Find the position in the previous row
        parent = (k + 1) // 2

        value = self.kthGrammar(n - 1, parent)

        # If k is odd, symbol stays the same
        if k % 2 == 1:
            return value

        # If k is even, symbol is flipped
        return 1 - value