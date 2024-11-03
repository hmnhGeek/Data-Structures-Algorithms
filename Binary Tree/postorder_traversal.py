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


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class PostOrder:
    @staticmethod
    def _recursive(root: Node, postorder):
        if root:
            PostOrder._recursive(root.left, postorder)
            PostOrder._recursive(root.right, postorder)
            postorder.append(root.data)

    @staticmethod
    def recursive(root: Node):
        postorder = []
        PostOrder._recursive(root, postorder)
        return postorder

    @staticmethod
    def iterative(root: Node):
        if root is None:
            return
        result = []
        stack = Stack()
        stack.push(root)

        while not stack.is_empty():
            node = stack.pop()
            result.append(node.data)
            if node.left is not None:
                stack.push(node.left)
            if node.right is not None:
                stack.push(node.right)

        result = result[-1:-len(result)-1:-1]
        return result

