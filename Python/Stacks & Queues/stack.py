# Problem link - https://www.tutorialspoint.com/javaexamples/data_stack.htm


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

    def top(self):
        if self.is_empty():
            return
        return self.head.data

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
        node = self.head
        data = self.head.data
        self.head = self.head.next
        del node
        self.length -= 1
        return data


# Example 1
stack = Stack()
for i in [1, 2, 3, 4]:
    stack.push(i)
while not stack.is_empty():
    print(stack.pop(), end=" ")
print()