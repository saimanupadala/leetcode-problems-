class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        depth = 0

        for child in root.children:
            depth = max(depth, self.maxDepth(child))

        return depth + 1