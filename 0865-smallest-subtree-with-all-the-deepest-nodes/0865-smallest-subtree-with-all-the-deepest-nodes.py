# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None, 0
            
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            
            # If left subtree is deeper, deepest nodes are on the left
            if left_depth > right_depth:
                return left_node, left_depth + 1
            # If right subtree is deeper, deepest nodes are on the right
            elif right_depth > left_depth:
                return right_node, right_depth + 1
            # If both depths are equal, current node is the LCA of deepest nodes
            else:
                return node, left_depth + 1
                
        return dfs(root)[0]