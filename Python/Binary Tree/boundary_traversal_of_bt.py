# Problem link - https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
# Solution - https://www.youtube.com/watch?v=0ca1nvR0be4&t=305s


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
            # prioritize left node first, then right, and if none, then it's a leaf node and break.
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
            # prioritize right node first, then left, and if none, then it's a leaf node and break.
            if root.right is not None:
                stack.push(root.data)
                root = root.right
            elif root.left is not None:
                stack.push(root.data)
                root = root.left
            else:
                break

        while not stack.length == 1:
            boundary.append(stack.pop())

    @staticmethod
    def boundary_traversal(root: TreeNode):
        """
            Time complexity will be O(N) and space complexity is O(N) using recursion for inorder traversal.
        """

        boundary = []
        # This will take O(H) time
        Solution._traverse_left_boundary_excluding_leaf(root, boundary)
        # This will take O(N) time
        Solution._inorder_traversal_for_leaf_nodes(root, boundary)
        # This will take O(H) time
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

# Example 2
n1, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)
n1.left = n2
n2.left = n4
n2.right = n9
n4.left = n6
n4.right = n5
n9.right = n3
n3.left = n7
n3.right = n8
Solution.boundary_traversal(n1)

# Example 3
n1, n2, n3, n4 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
n1.right = n2
n2.right = n3
n3.right = n4
Solution.boundary_traversal(n1)

# Example 4
n1, n2, n3, n4, n5, n6, n7, n8, n9 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7), TreeNode(8), TreeNode(9)
n10, n11, n12, n13 = TreeNode(10), TreeNode(11), TreeNode(12), TreeNode(13)
n1.left = n2
n2.left = n4
n4.left = n7
n5.left = n8
n10.left = n12
n1.right = n3
n3.right = n6
n6.right = n10
n2.right = n5
n5.right = n9
n7.right = n11
n11.right = n13
Solution.boundary_traversal(n1)
