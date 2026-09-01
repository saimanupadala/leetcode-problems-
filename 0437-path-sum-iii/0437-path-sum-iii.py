class Solution:
    def pathSum(self, root, targetSum):
        prefix = {0: 1}

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            # Number of paths ending at current node
            # whose sum is targetSum
            count = prefix.get(current_sum - targetSum, 0)

            # Add current prefix sum
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            # Search left and right subtrees
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            # Backtrack
            prefix[current_sum] -= 1

            return count

        return dfs(root, 0)
        