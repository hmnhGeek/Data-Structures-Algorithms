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

    def push_front(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
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
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        if self.head is not None:
            self.head.prev = None
        return item

    def pop_back(self):
        if self.is_empty():
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        del node
        self.length -= 1
        if self.tail is not None:
            self.tail.next = None
        return item


class Stack:
    def __init__(self):
        self.deque = Deque()

    def is_empty(self):
        return self.deque.is_empty()

    def length(self):
        return self.deque.length

    def push(self, x):
        self.deque.push_back(x)

    def pop(self):
        return self.deque.pop_back()


stack = Stack()
for i in [1, 2, 3, 4]:
    stack.push(i)

while not stack.is_empty():
    print(stack.pop())
