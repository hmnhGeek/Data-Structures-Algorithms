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


class TreeNode:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class Solution:
    @staticmethod
    def _traverse_left_boundary_excluding_leaf(root: TreeNode, boundary: list):
        while 1:
            if root.left is not None:
                boundary.append(root.data)
                root = root.left
            elif root.right is not None:
                boundary.append(root.data)
                root = root.right
            else:
                break

    @staticmethod
    def _inorder_traversal_for_leaf_nodes(root: TreeNode, boundary: list):
        if root:
            Solution._inorder_traversal_for_leaf_nodes(root.left, boundary)
            if root.left is None and root.right is None:
                boundary.append(root.data)
            Solution._inorder_traversal_for_leaf_nodes(root.right, boundary)

    @staticmethod
    def _traverse_right_boundary_excluding_leaf(root: TreeNode, boundary: list):
        stack = Stack()
        while 1:
            if root.right is not None:
                stack.push(root.data)
                root = root.right
            elif root.left is not None:
                stack.push(root.data)
                root = root.left
            else:
                break

        while not stack.is_empty():
            boundary.append(stack.pop())

    @staticmethod
    def boundary_traversal(root: TreeNode):
        boundary = []
        Solution._traverse_left_boundary_excluding_leaf(root, boundary)
        Solution._inorder_traversal_for_leaf_nodes(root, boundary)
        Solution._traverse_right_boundary_excluding_leaf(root, boundary)
        print(boundary)


# Example 1
n1, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n5.left = n8
n5.right = n9
Solution.boundary_traversal(n1)