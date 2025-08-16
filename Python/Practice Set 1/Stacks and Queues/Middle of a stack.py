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
        if self.length == 0:
            self.head = self.tail = None
        return item

    def pop_back(self):
        if self.is_empty():
            return
        item = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return item


class CustomStack:
    def __init__(self):
        self.stack = Stack()
        self.deque = Deque()

    def push(self, x):
        self.deque.push_back(x)
        if self.deque.length - self.stack.length > 1:
            item = self.deque.pop_front()
            self.stack.push(item)

    def pop(self):
        if self.deque.is_empty():
            return
        item = self.deque.pop_back()
        if self.stack.length > self.deque.length:
            temp = self.stack.pop()
            self.deque.push_front(temp)
        return item

    def get_middle(self):
        if self.deque.is_empty():
            return
        item = self.deque.head.data
        return item

    def pop_middle(self):
        if self.deque.is_empty():
            return
        item = self.deque.pop_front()
        if self.stack.length > self.deque.length:
            temp = self.stack.pop()
            self.deque.push_front(temp)
        return item


stack1 = CustomStack()
stack1.push(1)
stack1.push(2)
print(stack1.get_middle())
print(stack1.pop())
print(stack1.pop_middle())
