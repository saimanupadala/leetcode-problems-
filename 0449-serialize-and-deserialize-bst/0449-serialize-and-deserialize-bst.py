class Codec:

    def serialize(self, root):
        if not root:
            return ""

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(str(node.val))

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return ",".join(result)

    def deserialize(self, data):
        if not data:
            return None

        values = list(map(int, data.split(",")))

        root = TreeNode(values[0])
        stack = [root]

        for value in values[1:]:
            node = TreeNode(value)

            if value < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and value > stack[-1].val:
                    parent = stack.pop()

                parent.right = node

            stack.append(node)

        return root