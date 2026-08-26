class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)
            rob = node.val + left_not_rob + right_not_rob
            not_rob = max(left_rob, left_not_rob) + \
                      max(right_rob, right_not_rob)
            return (rob, not_rob)
        rob_root, not_rob_root = dfs(root)
        return max(rob_root, not_rob_root)
        