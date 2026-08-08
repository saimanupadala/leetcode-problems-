class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None
        clones = {}
        def dfs(node):
            if node in clones:
                return clones[node]
            copy = Node(node.val)
            clones[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
        