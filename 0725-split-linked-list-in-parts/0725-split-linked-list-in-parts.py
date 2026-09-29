class Solution:
    def splitListToParts(self, head, k):
        # Find total number of nodes
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        # Minimum size of each part
        size = n // k

        # Number of parts that get one extra node
        extra = n % k

        result = []

        curr = head

        for i in range(k):
            # First 'extra' parts get one additional node
            part_size = size + (1 if i < extra else 0)

            part_head = curr

            # Move to the end of this part
            for j in range(part_size - 1):
                curr = curr.next

            # Cut the linked list
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            result.append(part_head)

        return result