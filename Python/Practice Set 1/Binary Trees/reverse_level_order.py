class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


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


class Solution:
    @staticmethod
    def reverse_level_order(root: TreeNode):
        queue = Queue()
        queue.push(root)
        level_order = []
        while not queue.is_empty():
            node = queue.pop()
            level_order.append(node.data)
            if node.right is not None:
                queue.push(node.right)
            if node.left is not None:
                queue.push(node.left)
        return level_order[-1:-len(level_order)-1:-1]

