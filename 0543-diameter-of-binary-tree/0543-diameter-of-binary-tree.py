class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Longest path passing through this node
            self.diameter = max(self.diameter, left + right)

            # Return height of this node
            return 1 + max(left, right)

        height(root)

        return self.diameter