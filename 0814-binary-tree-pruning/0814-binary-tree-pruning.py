# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # 1. Post-order traversal: recurse on left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        # 2. If the current node is a leaf with value 0, prune it
        if root.val == 0 and not root.left and not root.right:
            return None
        
        return root