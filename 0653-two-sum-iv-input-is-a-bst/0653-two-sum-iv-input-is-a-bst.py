class Solution:
    def findTarget(self, root, k):
        seen = set()

        def dfs(node):
            if not node:
                return False

            # Required value to make sum k
            complement = k - node.val

            if complement in seen:
                return True

            seen.add(node.val)

            return dfs(node.left) or dfs(node.right)

        return dfs(root)        