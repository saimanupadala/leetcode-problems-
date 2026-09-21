class Solution:
    def printTree(self, root):
        # Find height of tree
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        h = height(root)

        # Rows = h + 1
        # Columns = 2^(h+1) - 1
        rows = h + 1
        cols = 2 ** rows - 1

        # Create empty matrix
        res = [["" for _ in range(cols)] for _ in range(rows)]

        # Place nodes
        def fill(node, r, c):
            if not node:
                return

            res[r][c] = str(node.val)

            if r < h:
                offset = 2 ** (h - r - 1)

                fill(node.left, r + 1, c - offset)
                fill(node.right, r + 1, c + offset)

        # Root goes in the middle
        fill(root, 0, (cols - 1) // 2)

        return res 