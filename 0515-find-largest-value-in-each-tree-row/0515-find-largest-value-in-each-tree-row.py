class Solution:
    def largestValues(self, root):
        if not root:
            return []

        queue = [root]
        answer = []

        while queue:
            size = len(queue)
            maximum = float('-inf')

            for i in range(size):
                node = queue.pop(0)

                maximum = max(maximum, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            answer.append(maximum)

        return answer