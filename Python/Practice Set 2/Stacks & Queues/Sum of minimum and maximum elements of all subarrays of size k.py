class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def push(self, x):
        node = Node(x)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_front(self):
        if self.length == 0:
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        del node
        self.length -= 1
        return item

    def pop_back(self):
        if self.length == 0:
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del node
        self.length -= 1
        return item

    def front(self):
        if self.length == 0:
            return
        return self.head.data

