class Solution:
    def isSubtree(self, root, subRoot):
        
        def sameTree(a, b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            return sameTree(a.left, b.left) and \
                   sameTree(a.right, b.right)

        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)