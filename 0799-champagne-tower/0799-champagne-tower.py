class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Create the tower
        glasses = [[0.0] * 100 for _ in range(100)]

        glasses[0][0] = poured

        for i in range(99):
            for j in range(i + 1):
                # Excess champagne
                extra = (glasses[i][j] - 1) / 2

                if extra > 0:
                    glasses[i + 1][j] += extra
                    glasses[i + 1][j + 1] += extra

        # A glass can hold at most 1 cup
        return min(1.0, glasses[query_row][query_glass])