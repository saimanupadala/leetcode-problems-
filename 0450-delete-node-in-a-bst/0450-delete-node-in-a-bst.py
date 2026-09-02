class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

    
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
         
            if not root.left:
                return root.right

         
            if not root.right:
                return root.left

            temp = root.right

            while temp.left:
                temp = temp.left

           
            root.val = temp.val

            
            root.right = self.deleteNode(root.right, temp.val)

        return root