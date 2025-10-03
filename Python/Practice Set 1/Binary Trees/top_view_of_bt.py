# Problem link - https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
# Solution - https://www.youtube.com/watch?v=Et9OCDNvJ78&t=206s


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
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_top_view(root: TreeNode):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        d = dict()
        mi, ma = 1e6, -1e6
        stack = Stack()
        stack.push((root, 0))
        result = []
        while not stack.is_empty():
            node, level = stack.pop()
            mi = min(mi, level)
            ma = max(ma, level)
            if level not in d:
                d[level] = node.data
            if node.left is not None:
                stack.push((node.left, level - 1))
            if node.right is not None:
                stack.push((node.right, level + 1))
        for i in range(mi, ma + 1):
            result.append(d[i])
        print(result)
        print()


# Example 1
n1, n2, n3, n4, n5, n6, n7 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n6
n3.right = n7
Solution.get_top_view(n1)


# Example 2
n10, n20, n30, n40, n60, n90, n100 = TreeNode(10), TreeNode(20), TreeNode(30), TreeNode(40), TreeNode(60), TreeNode(90), TreeNode(100)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
n30.left = n90
n30.right = n100
Solution.get_top_view(n10)


# Example 3
n1, n2, n3, n4, n5, n6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
n1.left = n2
n1.right = n3
n2.right = n4
n4.right = n5
n5.right = n6
Solution.get_top_view(n1)


# Example 4
n1, n2, n3, n4, n5, n6, n9, n10, n11 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(9), TreeNode(10), TreeNode(11)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n10
n4.right = n5
n5.right = n6
n3.left = n9
n3.right = n11
Solution.get_top_view(n1)
