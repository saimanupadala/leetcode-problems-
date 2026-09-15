class Solution:
    def preorder(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            # Visit root
            result.append(node.val)

            # Visit all children
            for child in node.children:
                dfs(child)

        dfs(root)
        return result
