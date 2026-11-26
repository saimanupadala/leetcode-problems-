class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def solve(n):
            if n in memo:
                return memo[n]

            if n == 1:
                return [TreeNode(0)]

            res = []

            for left in range(1, n, 2):
                right = n - 1 - left

                left_trees = solve(left)
                right_trees = solve(right)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)

            memo[n] = res
            return res

        if n % 2 == 0:
            return []

        return solve(n)