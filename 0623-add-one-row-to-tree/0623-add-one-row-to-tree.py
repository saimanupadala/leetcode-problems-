class Solution:
    def addOneRow(self, root, val, depth):
        # If we need to add the row at depth 1
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, current_depth):
            if node is None:
                return

            # We are at depth just before the required depth
            if current_depth == depth - 1:
                old_left = node.left
                old_right = node.right

                node.left = TreeNode(val)
                node.right = TreeNode(val)

                node.left.left = old_left
                node.right.right = old_right
                return

            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

        dfs(root, 1)
        return root