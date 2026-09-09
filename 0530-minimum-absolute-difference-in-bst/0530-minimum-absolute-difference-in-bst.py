class Solution:
    def getMinimumDifference(self, root):
        self.prev = None
        self.ans = float('inf')

        def inorder(node):
            if node is None:
                return

            # Left
            inorder(node.left)

            # Current
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)

            self.prev = node.val

            # Right
            inorder(node.right)

        inorder(root)

        return self.ans