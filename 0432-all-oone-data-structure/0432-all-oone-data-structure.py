class AllOne:

    class Node:
        def __init__(self, count):
            self.count = count
            self.keys = set()
            self.prev = None
            self.next = None

    def __init__(self):
        # Dummy head and tail
        self.head = self.Node(0)
        self.tail = self.Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        # key -> Node
        self.mp = {}

    def inc(self, key):
        # Key does not exist
        if key not in self.mp:
            # Check whether count 1 node already exists
            if self.head.next != self.tail and self.head.next.count == 1:
                node = self.head.next
            else:
                node = self.Node(1)
                self._insert_after(self.head, node)

            node.keys.add(key)
            self.mp[key] = node

        else:
            current = self.mp[key]
            new_count = current.count + 1

            # Check whether next node has required count
            if (current.next != self.tail and
                    current.next.count == new_count):
                next_node = current.next
            else:
                next_node = self.Node(new_count)
                self._insert_after(current, next_node)

            next_node.keys.add(key)
            self.mp[key] = next_node

            current.keys.remove(key)

            # Remove empty node
            if not current.keys:
                self._remove_node(current)

    def dec(self, key):
        current = self.mp[key]

        # Count becomes 0
        if current.count == 1:
            current.keys.remove(key)
            del self.mp[key]

            if not current.keys:
                self._remove_node(current)

        else:
            new_count = current.count - 1

            # Check whether previous node has required count
            if (current.prev != self.head and
                    current.prev.count == new_count):
                prev_node = current.prev
            else:
                prev_node = self.Node(new_count)
                self._insert_after(current.prev, prev_node)

            prev_node.keys.add(key)
            self.mp[key] = prev_node

            current.keys.remove(key)

            # Remove empty node
            if not current.keys:
                self._remove_node(current)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))

    # Insert new_node after prev_node
    def _insert_after(self, prev_node, new_node):
        new_node.next = prev_node.next
        new_node.prev = prev_node

        prev_node.next.prev = new_node
        prev_node.next = new_node

    # Remove a node from linked list
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev