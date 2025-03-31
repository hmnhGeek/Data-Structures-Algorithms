class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


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
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def flatten(root):
        stack = Stack()
        stack.push(root)
        while not stack.is_empty():
            curr = stack.pop()
            if curr.right is not None:
                stack.push(curr.right)
            if curr.left is not None:
                stack.push(curr.left)
            if not stack.is_empty():
                curr.right = stack.head.data
            curr.left = None


# Example 1
n10, n12, n15, n25, n30, n36 = Node(10), Node(12), Node(15), Node(25), Node(30), Node(36)
n10.left = n12
n10.right = n15
n12.left = n25
n12.right = n30
n15.left = n36
Solution.flatten(n10)
curr = n25
while curr is not None:
    print(curr.data, end=" ")
    curr = curr.right
