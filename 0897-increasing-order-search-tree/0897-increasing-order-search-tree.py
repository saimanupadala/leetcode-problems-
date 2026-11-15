
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        dummy = TreeNode(0)
        curr = dummy

        for val in values:
            curr.right = TreeNode(val)
            curr = curr.right

        return dummy.right
