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
        self.head = self.head.next
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def print_diagonal_traversal(root):
        queue = Queue()
        while root is not None:
            queue.push(root)
            root = root.right
        result = []
        while not queue.is_empty():
            node = queue.pop()
            result.append(node.data)
            left_node = node.left
            while left_node is not None:
                queue.push(left_node)
                left_node = left_node.right
        print(result)


# Example 1
n8, n3, n10, n1, n6, n14, n4, n7, n13 = TreeNode(8), TreeNode(3), TreeNode(10), TreeNode(1), TreeNode(6), TreeNode(14), TreeNode(4), TreeNode(7), TreeNode(13)
n8.left = n3
n8.right = n10
n3.left = n1
n3.right = n6
n10.right = n14
n6.left = n4
n6.right = n7
n14.left = n13
Solution.print_diagonal_traversal(n8)


# Example 2
n1, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.left = n9
Solution.print_diagonal_traversal(n1)


# Example 3
n1, n2, n3, n4, n5, n6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
Solution.print_diagonal_traversal(n1)


# Example 4
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
Solution.print_diagonal_traversal(n1)


# Example 5
n1, n2, n3, n4, n5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
Solution.print_diagonal_traversal(n1)


# Example 6
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n8, n9, n10, n11 = TreeNode(8), TreeNode(9), TreeNode(10), TreeNode(11)
n1.left = n2
n1.right = n7
n2.left = n3
n7.right = n8
n3.right = n4
n8.left = n9
n4.left = n5
n4.right = n6
n9.left = n10
n9.right = n11
Solution.print_diagonal_traversal(n1)