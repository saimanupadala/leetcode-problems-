class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        swaps = 0

        for i in range(0, len(row), 2):
            partner = row[i] ^ 1

            # Already sitting together
            if row[i + 1] == partner:
                continue

            # Find partner
            j = i + 1
            while row[j] != partner:
                j += 1

            # Swap partner into i+1
            row[i + 1], row[j] = row[j], row[i + 1]

            swaps += 1

        return swaps