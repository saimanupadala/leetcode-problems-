class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        result = []

        def dfs(node):
            for digit in range(k):
                edge = node + str(digit)

                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    result.append(str(digit))

        start = "0" * (n - 1)
        dfs(start)

        return "".join(result) + start