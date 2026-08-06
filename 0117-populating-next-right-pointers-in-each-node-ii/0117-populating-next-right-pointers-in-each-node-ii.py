# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return root
        curr = root
        while curr:
            head = None   
            prev = None   
            while curr:
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right
                curr = curr.next
            curr = head
        return root
        