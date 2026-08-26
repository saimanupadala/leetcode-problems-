class Solution:
    def isValidSerialization(self, preorder):
        slots = 1

        for node in preorder.split(','):
            # Every node needs one available slot
            if slots == 0:
                return False

            if node == '#':
                slots -= 1
            else:

                slots += 1

        return slots == 0
        