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
            return -1
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        item = self.s2.pop()
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
        return item


# Example 1
q1 = Queue()
q1.push(2)
q1.push(3)
print(q1.pop())
q1.push(4)
print(q1.pop())

# Example 2
q2 = Queue()
q2.push(2)
print(q2.pop())
print(q2.pop())