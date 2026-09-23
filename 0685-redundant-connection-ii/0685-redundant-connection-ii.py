class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        def valid_tree(skip):
            parent = list(range(n + 1))
            indegree = [0] * (n + 1)

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            for i, (u, v) in enumerate(edges):
                if i == skip:
                    continue

                # A node cannot have two parents
                indegree[v] += 1
                if indegree[v] > 1:
                    return False

                # Check for cycle
                pu = find(u)
                pv = find(v)

                if pu == pv:
                    return False

                parent[pv] = pu

            return True

        # Check from last edge to first edge
        for i in range(n - 1, -1, -1):
            if valid_tree(i):
                return edges[i]

        return []