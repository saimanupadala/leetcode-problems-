# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int):
        def solve(start, end):
            if start > end:
                return [None]
            ans = []
            for i in range(start, end + 1):
                left = solve(start, i - 1)
                right = solve(i + 1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        return solve(1, n)
        