
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        answer = [0] * n

        def dfs1(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue

                dfs1(child, node)
                count[node] += count[child]
                answer[node] += answer[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue

                answer[child] = answer[node] - count[child] + (n - count[child])
                dfs2(child, node)

        dfs1(0, -1)
        dfs2(0, -1)

        return answer
