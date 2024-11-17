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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_zig_zag_traversal(root: Node):
        stack = Stack()
        queue = Queue()

        left_to_right = True
        queue.push(root)

        while 1:
            while not queue.is_empty():
                node = queue.pop()
                print(node.data, end=" ")
                if left_to_right:
                    if node.left is not None:
                        stack.push(node.left)
                    if node.right is not None:
                        stack.push(node.right)
                else:
                    if node.right is not None:
                        stack.push(node.right)
                    if node.left is not None:
                        stack.push(node.left)

            while not stack.is_empty():
                queue.push(stack.pop())
            left_to_right = not left_to_right
            if queue.is_empty() and stack.is_empty():
                print()
                break


# Example 1
n5, n1, n9, n3, n2, n8, n4 = TreeNode(5), TreeNode(1), TreeNode(9), TreeNode(3), TreeNode(2), TreeNode(8), TreeNode(4)
n5.left = n1
n5.right = n9
n1.left = n3
n1.right = n2
n9.left = n8
n9.right = n4
Solution.get_zig_zag_traversal(n5)

# Example 2
n7, n9, n71, n8, n81, n6, n10, n91 = TreeNode(7), TreeNode(9), TreeNode(7), TreeNode(8), TreeNode(8), TreeNode(6), TreeNode(10), TreeNode(9)
n7.left = n9
n7.right = n71
n9.left = n8
n9.right = n81
n71.left = n6
n8.left = n10
n8.right = n91
Solution.get_zig_zag_traversal(n7)

# Example 3
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
Solution.get_zig_zag_traversal(n1)