class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            steps = self.count_steps(n, current, current + 1)

            if steps <= k:
                # Skip this prefix
                current += 1
                k -= steps
            else:
                # Go deeper into this prefix
                current *= 10
                k -= 1

        return current

    def count_steps(self, n: int, prefix: int, next_prefix: int) -> int:
        steps = 0

        while prefix <= n:
            steps += min(n + 1, next_prefix) - prefix
            prefix *= 10
            next_prefix *= 10

        return steps
        