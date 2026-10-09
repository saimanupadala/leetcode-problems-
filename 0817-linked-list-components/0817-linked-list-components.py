# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        nums_set = set(nums)
        components = 0
        curr = head
        
        while curr:
            # Check if current node's value is in nums
            # AND it marks the end of a connected segment
            if curr.val in nums_set and (not curr.next or curr.next.val not in nums_set):
                components += 1
            curr = curr.next
            
        return components