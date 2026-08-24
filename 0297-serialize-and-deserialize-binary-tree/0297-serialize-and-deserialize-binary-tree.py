class Codec:

    def serialize(self, root):
        result = []

        def preorder(node):
            if node is None:
                result.append("N")
                return

            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

    def deserialize(self, data):
        values = iter(data.split(","))

        def build():
            value = next(values)

            if value == "N":
                return None

            node = TreeNode(int(value))
            node.left = build()
            node.right = build()

            return node

        return build()