class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total = sum(matchsticks)

        # A square has 4 equal sides
        if total % 4 != 0:
            return False

        side = total // 4

        # Try longer sticks first
        matchsticks.sort(reverse=True)

        # Length of the 4 sides
        sides = [0, 0, 0, 0]

        def backtrack(index):
            if index == len(matchsticks):
                return True

            stick = matchsticks[index]

            for i in range(4):
                # Don't exceed required side length
                if sides[i] + stick > side:
                    continue

                # Avoid trying identical side states
                if i > 0 and sides[i] == sides[i - 1]:
                    continue

                sides[i] += stick

                if backtrack(index + 1):
                    return True

                sides[i] -= stick

            return False

        return backtrack(0)