class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _check(root: Node, low, high):
        if root.left is None and root.right is None:
            return low < root.data < high

        if low < root.data < high:
            left = True
            if root.left is not None:
                left = Solution._check(root.left, low, root.data)

            right = True
            if root.right is not None:
                right = Solution._check(root.right, root.data, high)

            return left and right
        else:
            return False

    @staticmethod
    def is_bst(root: Node):
        if root is None:
            return True
        return Solution._check(root, -1e6, 1e6)


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