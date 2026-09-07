class Solution:
    def findBottomLeftValue(self, root):
        queue = [root]

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)

                # First node of the current level
                if i == 0:
                    answer = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return answer 