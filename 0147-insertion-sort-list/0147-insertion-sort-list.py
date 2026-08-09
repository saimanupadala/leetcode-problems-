class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        current = head
        while current:
            next_node = current.next
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = next_node
        return dummy.next
        