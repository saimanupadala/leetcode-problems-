class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)

        # 0 = unvisited
        # 1 = visiting
        # 2 = safe
        state = [0] * n

        def dfs(node):
            if state[node] == 1:
                return False   # Cycle found

            if state[node] == 2:
                return True    # Already known to be safe

            state[node] = 1    # Mark as visiting

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            state[node] = 2    # All neighbors are safe
            return True

        answer = []

        for i in range(n):
            if dfs(i):
                answer.append(i)

        return answer