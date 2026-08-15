class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        