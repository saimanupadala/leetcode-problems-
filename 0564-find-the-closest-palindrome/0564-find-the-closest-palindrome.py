class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        length = len(n)

        # Special case
        if num <= 10:
            return str(num - 1)

        # Boundary candidates
        candidates = {
            10 ** (length - 1) - 1,
            10 ** length + 1
        }

        # Take the first half
        half = (length + 1) // 2
        prefix = int(n[:half])

        # Try prefix-1, prefix, prefix+1
        for p in [prefix - 1, prefix, prefix + 1]:
            s = str(p)

            if length % 2 == 0:
                palindrome = s + s[::-1]
            else:
                palindrome = s + s[-2::-1]

            candidates.add(int(palindrome))

        # Remove n itself
        candidates.discard(num)

        # Find closest; if tie, choose smaller
        return str(min(candidates, key=lambda x: (abs(x - num), x)))