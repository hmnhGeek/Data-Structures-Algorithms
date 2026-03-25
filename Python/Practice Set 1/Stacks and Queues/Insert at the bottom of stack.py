class Node:
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
        node = Node(x)
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

    def insert_at_bottom(self, x):
        node = Node(x)
        if self.is_empty():
            self.push(x)
            return
        self.tail.next = node
        self.tail = node
        self.length += 1


stack = Stack()
for i in [1, 2, 3, 4]:
    stack.push(i)
stack.insert_at_bottom(10)
while not stack.is_empty():
    print(stack.pop(), end= " ")
