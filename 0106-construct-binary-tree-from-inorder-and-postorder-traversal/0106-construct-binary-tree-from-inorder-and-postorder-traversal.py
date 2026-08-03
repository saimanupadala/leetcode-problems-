# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {value: i for i, value in enumerate(inorder)}
        postorder_index = len(postorder) - 1
        def build(left, right):
            nonlocal postorder_index
            if left > right:
                return None
            root_val = postorder[postorder_index]
            postorder_index -= 1
            root = TreeNode(root_val)
            index = inorder_map[root_val]
            root.right = build(index + 1, right)
            root.left = build(left, index - 1)
            return root
        return build(0, len(inorder) - 1)
        