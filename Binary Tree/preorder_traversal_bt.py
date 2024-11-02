class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


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


class Preorder:
    @staticmethod
    def _recursive(root: Node, preorder):
        if root:
            preorder.append(root.data)
            Preorder._recursive(root.left, preorder)
            Preorder._recursive(root.right, preorder)

    @staticmethod
    def recursive(root: Node):
        preorder = []
        Preorder._recursive(root, preorder)
        return preorder

    @staticmethod
    def iterative(root: Node):
        stack = Stack()
        preorder = []
        stack.push(root)

        while not stack.is_empty():
            node = stack.pop()
            preorder.append(node.data)

            if node.right is not None:
                stack.push(node.right)
            if node.left is not None:
                stack.push(node.left)

        return preorder


# Example 1
n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.left = n2
n2.left = n4
n3.left = n5
n5.left = n7
n1.right = n3
n3.right = n6
n5.right = n8
print(Preorder.recursive(n1))
print()
print(Preorder.iterative(n1))