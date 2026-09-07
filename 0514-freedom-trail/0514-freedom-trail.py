class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from functools import lru_cache

        n = len(ring)

        # Store positions of each character in ring
        positions = {}

        for i, ch in enumerate(ring):
            positions.setdefault(ch, []).append(i)

        @lru_cache(None)
        def dp(ring_pos, key_pos):
            if key_pos == len(key):
                return 0

            ans = float('inf')

            # Try every occurrence of the required character
            for next_pos in positions[key[key_pos]]:
                # Clockwise distance
                clockwise = abs(next_pos - ring_pos)

                # Anticlockwise distance
                anticlockwise = n - clockwise

                rotate = min(clockwise, anticlockwise)

                # +1 for pressing the center button
                steps = rotate + 1

                ans = min(
                    ans,
                    steps + dp(next_pos, key_pos + 1)
                )

            return ans

        return dp(0, 0)