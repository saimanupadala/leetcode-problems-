class Solution:
    def findDuplicateSubtrees(self, root):
        from collections import defaultdict

        count = defaultdict(int)
        ids = {}
        result = []
        next_id = 1

        def dfs(node):
            nonlocal next_id

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            key = (node.val, left, right)

            if key not in ids:
                ids[key] = next_id
                next_id += 1

            subtree_id = ids[key]
            count[subtree_id] += 1

            if count[subtree_id] == 2:
                result.append(node)

            return subtree_id

        dfs(root)
        return result