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
    def _preorder(root, preorder):
        if root:
            preorder.append(root.data)
            Solution._preorder(root.left, preorder)
            Solution._preorder(root.right, preorder)

    @staticmethod
    def preorder_recursive(root):
        preorder = []
        Solution._preorder(root, preorder)
        return preorder