class Solution:
    def outerTrees(self, trees):
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - \
                   (a[1] - o[1]) * (b[0] - o[0])

        trees.sort()

        # Build lower hull
        lower = []
        for p in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Combine both hulls
        return [list(p) for p in set(map(tuple, lower + upper))]