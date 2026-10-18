class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        xs = sorted(set(x for r in rectangles for x in (r[0], r[2])))
        area = 0

        for i in range(len(xs) - 1):
            x1, x2 = xs[i], xs[i + 1]
            ys = []

            for a, b, c, d in rectangles:
                if a <= x1 and c >= x2:
                    ys.append((b, d))

            ys.sort()
            height = 0
            if ys:
                start, end = ys[0]

                for bottom, top in ys[1:]:
                    if bottom > end:
                        height += end - start
                        start, end = bottom, top
                    else:
                        end = max(end, top)

                height += end - start

            area = (area + (x2 - x1) * height) % MOD

        return area