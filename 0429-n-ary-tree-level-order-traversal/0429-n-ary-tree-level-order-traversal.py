from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

         
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

         
                for child in node.children:
                    queue.append(child)

            result.append(level)

        return result
        