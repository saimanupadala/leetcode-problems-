class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1

        i2 = i3 = i5 = 0

        for i in range(1, n):
            next2 = ugly[i2] * 2
            next3 = ugly[i3] * 3
            next5 = ugly[i5] * 5

            ugly[i] = min(next2, next3, next5)

            if ugly[i] == next2:
                i2 += 1
            if ugly[i] == next3:
                i3 += 1
            if ugly[i] == next5:
                i5 += 1

        return ugly[n - 1]
        