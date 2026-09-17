class Solution:
    def tree2str(self, root):
        if root is None:
            return ""

        result = str(root.val)

        # Left child exists
        if root.left:
            result += "(" + self.tree2str(root.left) + ")"

        # Right child exists
        if root.right:
            # If no left child, we must add ()
            if not root.left:
                result += "()"
            result += "(" + self.tree2str(root.right) + ")"

        return result