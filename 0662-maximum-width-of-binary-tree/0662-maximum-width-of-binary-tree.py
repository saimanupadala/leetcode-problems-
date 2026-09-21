from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        # Store (node, index)
        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            level_length = len(queue)
            first_index = queue[0][1]

            for _ in range(level_length):
                node, index = queue.popleft()

                # Normalize index to avoid very large numbers
                index -= first_index

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))

            # Width of current level
            max_width = max(max_width, index + 1)

        return max_width