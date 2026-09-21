class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        # Find maximum value and its index
        max_val = max(nums)
        index = nums.index(max_val)

        # Create root
        root = TreeNode(max_val)

        # Build left and right subtrees
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])

        return root