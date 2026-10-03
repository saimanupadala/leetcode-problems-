class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # Remove X and compare remaining characters
        if start.replace("X", "") != result.replace("X", ""):
            return False

        i = j = 0
        n = len(start)

        while i < n and j < n:
            # Skip X
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1

            # Both reached the end
            if i == n or j == n:
                return i == n and j == n

            # L can only move to the left
            if start[i] == 'L' and i < j:
                return False

            # R can only move to the right
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True