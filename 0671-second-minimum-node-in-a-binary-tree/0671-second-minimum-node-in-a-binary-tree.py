class Solution:
    def findSecondMinimumValue(self, root):
        first = root.val
        second = float('inf')

        def dfs(node):
            nonlocal second

            if not node:
                return

            if first < node.val < second:
                second = node.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if second == float('inf'):
            return -1

        return second