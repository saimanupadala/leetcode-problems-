class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)