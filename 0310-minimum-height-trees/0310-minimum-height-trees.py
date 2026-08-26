from collections import deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        # Build the graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        # Add all leaf nodes
        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        # Remove leaves layer by layer
        while remaining > 2:
            leaves = len(queue)
            remaining -= leaves

            for _ in range(leaves):
                leaf = queue.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)
        