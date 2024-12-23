class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Dequeue:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def insert_first(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def insert_last(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def remove_first(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def remove_last(self):
        if self.is_empty():
            return
        item = self.tail.data
        node = self.tail
        self.tail = self.tail.prev
        del node
        self.length -= 1
        return item


class Stack:
    def __init__(self):
        self.dq = Dequeue()

    def is_empty(self):
        return self.dq.is_empty()

    def push(self, x):
        self.dq.insert_last(x)

    def pop(self):
        return self.dq.remove_last()


class Queue:
    def __init__(self):
        self.dq = Dequeue()

    def is_empty(self):
        return self.dq.is_empty()

    def push(self, x):
        self.dq.insert_last(x)

    def pop(self):
        return self.dq.remove_first()


# Example 1
stack = Stack()
for i in [2, 6, 8, 0, 9, 9, 7]:
    stack.push(i)
while not stack.is_empty():
    print(stack.pop(), end=" ")
print()