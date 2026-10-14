class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        def similar(a, b):
            diff = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False

            return len(diff) == 0 or (
                len(diff) == 2
                and a[diff[0]] == b[diff[1]]
                and a[diff[1]] == b[diff[0]]
            )

        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]):
                    union(i, j)

        return sum(1 for i in range(n) if find(i) == i)