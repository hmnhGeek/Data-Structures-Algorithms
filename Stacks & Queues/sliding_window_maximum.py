class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push_back(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_back(self):
        if self.is_empty():
            return
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del node
        self.length -= 1

    def pop_front(self):
        if self.is_empty():
            return
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        del node
        self.length -= 1

    def front(self):
        if self.is_empty():
            return -1
        return self.head.data


