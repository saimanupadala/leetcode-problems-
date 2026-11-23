
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        pos = {val: i for i, val in enumerate(postorder)}

        def build(preStart, preEnd, postStart, postEnd):

            if preStart > preEnd:
                return None

            root = TreeNode(preorder[preStart])

            if preStart == preEnd:
                return root

            leftRoot = preorder[preStart + 1]
            leftSize = pos[leftRoot] - postStart + 1

            root.left = build(
                preStart + 1,
                preStart + leftSize,
                postStart,
                postStart + leftSize - 1
            )

            root.right = build(
                preStart + leftSize + 1,
                preEnd,
                postStart + leftSize,
                postEnd - 1
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)

        