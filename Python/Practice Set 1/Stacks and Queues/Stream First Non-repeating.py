class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def front(self):
        if self.is_empty():
            return "#"
        return self.head.data

    def remove(self, node: Node):
        is_tail, is_head = False, False
        prev = node.prev
        next_node = node.next
        if prev:
            prev.next = next_node
        if next_node:
            next_node.prev = prev
        del node
        self.length -= 1
        if is_head:
            self.head = next_node
        if is_tail:
            self.tail = prev

