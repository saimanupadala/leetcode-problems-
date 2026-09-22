class Solution:
    def trimBST(self, root, low, high):
        if not root:
            return None

        # Root is smaller than the allowed range
        if root.val < low:
            return self.trimBST(root.right, low, high)

        # Root is larger than the allowed range
        if root.val > high:
            return self.trimBST(root.left, low, high)

        # Root is inside the range
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)

        return root