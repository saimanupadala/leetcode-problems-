class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        moves = 0
        total = 0

        while total < target or (total - target) % 2 != 0:
            moves += 1
            total += moves

        return moves