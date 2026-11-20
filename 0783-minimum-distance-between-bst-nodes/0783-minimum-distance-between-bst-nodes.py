class Solution:
    def minDiffInBST(self, root):
        self.prev = None
        self.ans = float('inf')

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)

            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.ans


