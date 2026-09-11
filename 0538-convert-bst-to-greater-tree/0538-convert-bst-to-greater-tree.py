class Solution:
    def convertBST(self, root):
        total = 0

        def dfs(node):
            nonlocal total

            if not node:
                return

            # Visit greater values first
            dfs(node.right)

            # Add sum of greater values
            total += node.val
            node.val = total

            # Visit smaller values
            dfs(node.left)

        dfs(root)
        return root