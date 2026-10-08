class Solution:
    def soupServings(self, n: int) -> float:
        # Optimization: For n >= 4800, probability is practically 1.0
        if n >= 4800:
            return 1.0

        # Scale down by 25 mL per unit
        units = (n + 24) // 25
        memo = {}

        def dp(a: int, b: int) -> float:
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5  # Both empty at the same time
            if a <= 0:
                return 1.0  # A empties first
            if b <= 0:
                return 0.0  # B empties first

            if (a, b) in memo:
                return memo[(a, b)]

            # Average probability across 4 equal operations
            prob = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

            memo[(a, b)] = prob
            return prob

        return dp(units, units)    