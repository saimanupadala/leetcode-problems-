class Solution:
    def allPathsSourceTarget(self, graph):
        result = []
        path = [0]

        def dfs(node):
            if node == len(graph) - 1:
                result.append(path[:])
                return

            for next_node in graph[node]:
                path.append(next_node)
                dfs(next_node)
                path.pop()

        dfs(0)
        return result