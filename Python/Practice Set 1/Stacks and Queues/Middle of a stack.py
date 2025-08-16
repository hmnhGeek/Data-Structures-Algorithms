class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = StackNode(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        self.head = self.head.next
        self.length -= 1
        return item


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push_front(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1

    def push_back(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop_front(self):
        if self.is_empty():
            return
        item = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        self.length -= 1
        return item

    def pop_back(self):
        if self.is_empty():
            return
        item = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        return item

