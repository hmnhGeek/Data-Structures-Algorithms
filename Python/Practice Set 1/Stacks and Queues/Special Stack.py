# Problem link - https://www.geeksforgeeks.org/problems/special-stack/1
# Solution - https://www.youtube.com/watch?v=NdDIaH91P0g


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


class SpecialStack:
    def __init__(self):
        self.stack = Stack()

    def push(self, x):
        if self.stack.is_empty():
            self.stack.push((x, x))
            return
        if self.stack.top()[1] > x:
            self.stack.push((x, x))
        else:
            self.stack.push((x, self.stack.top()[1]))

    def pop(self):
        if self.stack.is_empty():
            return
        item = self.stack.pop()[0]
        return item

    def get_min(self):
        if self.stack.is_empty():
            return
        return self.stack.top()[1]


class Solution:
    @staticmethod
    def test(*args):
        stack = SpecialStack()
        for i in args:
            stack.push(i)
            print(stack.get_min())


Solution.test(18, 19, 29, 15, 16)
print()
Solution.test(34, 335, 1814, 86)
print()
stack = SpecialStack()
stack.push(12)
stack.push(15)
stack.push(10)
print(stack.get_min())
print(stack.pop())
print(stack.get_min())
stack.push(10)
