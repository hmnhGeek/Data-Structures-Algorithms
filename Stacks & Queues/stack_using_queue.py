class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
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
            self.tail = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        while not self.q1.is_empty():
            self.q2.push(self.q1.pop())
        self.q1.push(x)
        while not self.q2.is_empty():
            self.q1.push(self.q2.pop())

    def pop(self):
        return self.q1.pop()


stack1 = Stack()
stack1.push(2)
stack1.push(3)
print(stack1.pop())
stack1.push(4)
print(stack1.pop())
print()
stack2 = Stack()
stack2.push(2)
print(stack2.pop())
print(stack2.pop())
stack2.push(3)
