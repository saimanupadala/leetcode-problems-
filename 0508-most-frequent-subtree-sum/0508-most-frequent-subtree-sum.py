class Solution:
    def findFrequentTreeSum(self, root):
        from collections import Counter

        count = Counter()

        def dfs(node):
            if not node:
                return 0

            # Calculate subtree sum
            total = node.val + dfs(node.left) + dfs(node.right)

            # Count this subtree sum
            count[total] += 1

            return total

        dfs(root)

        # Find maximum frequency
        max_freq = max(count.values())

        # Return all sums having maximum frequency
        return [s for s in count if count[s] == max_freq]