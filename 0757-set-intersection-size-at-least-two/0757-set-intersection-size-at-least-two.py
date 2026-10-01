class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = -1
        b = -1
        ans = 0

        for start, end in intervals:
            count = 0

            if a >= start:
                count += 1
            if b >= start:
                count += 1

            if count == 2:
                continue

            if count == 0:
                a = end - 1
                b = end
                ans += 2

            else:
                # One point is already inside.
                if a < start:
                    a = b
                    b = end
                else:
                    a = b
                    b = end
                ans += 1

        return ans