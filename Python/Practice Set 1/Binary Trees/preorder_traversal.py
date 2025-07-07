# Problem link - https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/


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
    def recursive(root):
        """
            Time and space complexity both are O(n).
        """
        preorder = []
        Solution._preorder(root, preorder)
        return preorder
    
    @staticmethod
    def iterative(root):
        """
            Time and space complexity both are O(n).
        """
        stack = Stack()
        stack.push(root)
        result = []
        while not stack.is_empty():
            node = stack.pop()
            result.append(node.data)
            if node.right is not None:
                stack.push(node.right)
            if node.left is not None:
                stack.push(node.left)
        return result
    

# Example 1
n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.left = n2
n2.left = n4
n3.left = n5
n5.left = n7
n1.right = n3
n3.right = n6
n5.right = n8
print(Solution.recursive(n1))
print()
print(Solution.iterative(n1))

print()
print()

# Example 2
n1, n2, n3, n4, n5, n6 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
n1.left = n2
n2.left = n4
n1.right = n3
n2.right = n5
n3.right = n6
print(Solution.recursive(n1))
print()
print(Solution.iterative(n1))