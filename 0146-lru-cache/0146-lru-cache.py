class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Add node right after head
    def add(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Mark as recently used
        self.remove(node)
        self.add(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]

            # Update value
            node.value = value

            # Move to front
            self.remove(node)
            self.add(node)

        else:
            node = Node(key, value)

            self.cache[key] = node
            self.add(node)

            # If capacity exceeded
            if len(self.cache) > self.capacity:
                # Least recently used node
                lru = self.tail.prev

                self.remove(lru)
                del self.cache[lru.key]


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None