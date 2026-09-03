class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        # Already reached the target
        if desiredTotal <= 0:
            return True

        # Sum of all available numbers is less than target
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False

        memo = {}

        def can_win(mask, remaining):
            if mask in memo:
                return memo[mask]

            for i in range(1, maxChoosableInteger + 1):

                # Check if i is already used
                if mask & (1 << i):
                    continue

                # If choosing i reaches the target, we win
                if i >= remaining:
                    memo[mask] = True
                    return True

                # Choose i and let opponent play
                new_mask = mask | (1 << i)

                # If opponent cannot win, we win
                if not can_win(new_mask, remaining - i):
                    memo[mask] = True
                    return True

            memo[mask] = False
            return False

        return can_win(0, desiredTotal)