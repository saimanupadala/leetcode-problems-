class Solution:
    def countArrangement(self, n: int) -> int:
        used = set()
        count = 0

        def backtrack(i):
            nonlocal count

            # All positions are filled
            if i > n:
                count += 1
                return

            for num in range(1, n + 1):
                if num not in used:
                    if num % i == 0 or i % num == 0:
                        used.add(num)

                        backtrack(i + 1)

                        used.remove(num)

        backtrack(1)
        return count 