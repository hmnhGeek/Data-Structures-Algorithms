class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def is_bst(node):
        return Solution._solve(node, -1e6, 1e6)

    @staticmethod
    def _solve(node, low, high):
        if node is None:
            return True
        if not (low <= node.data <= high):
            return False
        return Solution._solve(node.left, low, node.data) and Solution._solve(node.right, node.data, high)


# Example 1
n1, n2, n3, n5 = Node(1), Node(2), Node(3), Node(5)
n2.left = n1
n2.right = n3
n3.right = n5
print(Solution.is_bst(n2))

# Example 2
n2, n6, n7, n9 = Node(2), Node(6), Node(7), Node(9)
n2.right = n7
n7.right = n6
n6.right = n9
print(Solution.is_bst(n2))

# Example 3
n10, n5, n20, n9, n25 = Node(10), Node(5), Node(20), Node(9), Node(25)
n10.left = n5
n10.right = n20
n20.left = n9
n20.right = n25
print(Solution.is_bst(n10))

# Example 4
n1, n4, n5, n3, n6 = Node(1), Node(4), Node(5), Node(3), Node(6)
n5.left = n1
n5.right = n4
n4.left = n3
n4.right = n6
print(Solution.is_bst(n5))

# Example 5
n1, n2, n3 = Node(1), Node(2), Node(3)
n2.left = n1
n2.right = n3
print(Solution.is_bst(n2))
