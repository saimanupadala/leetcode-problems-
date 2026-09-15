class Solution:
    def postorder(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            # Visit all children first
            for child in node.children:
                dfs(child)

            # Visit root after children
            result.append(node.val)

        dfs(root)
        return result
