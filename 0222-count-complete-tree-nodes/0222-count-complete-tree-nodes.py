class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        def get_height(node):
            height = 0

            while node:
                height += 1
                node = node.left

            return height

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        # Left and right subtrees have the same height.
        if left_height == right_height:
            # Left subtree is perfect
            return (1 << left_height) + self.countNodes(root.right)

        else:
            # Right subtree is perfect
            return (1 << right_height) + self.countNodes(root.left)
        