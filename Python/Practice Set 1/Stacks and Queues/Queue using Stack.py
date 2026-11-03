# Problem link - https://www.geeksforgeeks.org/problems/queue-using-stack/1


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
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def top(self):
        if self.is_empty():
            return
        return self.head.data


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, x):
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

    def front(self):
        return self.s1.top()

    def size(self):
        return self.s1.length


# Example 1
q1 = Queue()
q1.enqueue(5)
q1.enqueue(3)
q1.enqueue(4)
print(q1.front())
print(q1.dequeue())
print(q1.size())
print(q1.front())

# Example 2
q2 = Queue()
print(q2.front())
print(q2.size())
q2.enqueue(10)
