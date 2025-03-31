# Problem link - https://www.geeksforgeeks.org/problems/sum-tree/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _check_sum_tree(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # if the root node is None, return 0 and a null node is always a sum tree.
        if root is None:
            return 0, True

        # if it's a leaf node, return its data and True because leaf node is sum tree.
        if root.left is None and root.right is None:
            return root.data, True

        # get the left subtree sum and if the left subtree is a sum tree or not
        left_ans, left_sum_tree = Solution._check_sum_tree(root.left)

        # get the right subtree sum and if the right subtree is a sum tree or not
        right_ans, right_sum_tree = Solution._check_sum_tree(root.right)

        # if both subtrees are sum trees and...
        if left_sum_tree and right_sum_tree:
            _sum = root.data + left_ans + right_ans

            # and if root's data == subtree data sums, then return this sum and true
            if root.data == left_ans + right_ans:
                return _sum, True
            else:
                # else return this sum (although it won't be used), and false as this subtree is not a sum tree.
                return _sum, False
        else:
            # if both subtrees are not sum trees, return 0 (will not be used) and false to denote that it is not a sum
            # tree.
            return 0, False

    @staticmethod
    def check_sum_tree(root: Node):
        _, result = Solution._check_sum_tree(root)
        return result


# Example 1
n1, n2, n3 = Node(1), Node(2), Node(3)
n3.left = n1
n3.right = n2
print(Solution.check_sum_tree(n3))


# Example 2
n10, n20, n30, n101, n102 = Node(10), Node(20), Node(30), Node(10), Node(10)
n10.left = n20
n10.right = n30
n20.left = n101
n20.right = n102
print(Solution.check_sum_tree(n10))


# Example 3
n26, n10, n3, n4, n6, n31 = Node(26), Node(10), Node(3), Node(4), Node(6), Node(3)
n26.left = n10
n26.right = n3
n10.left = n4
n10.right = n6
n3.right = n31
print(Solution.check_sum_tree(n26))


# Example 4
n26, n10, n3, n2, n6, n31 = Node(26), Node(10), Node(3), Node(2), Node(6), Node(3)
n26.left = n10
n26.right = n3
n10.left = n2
n10.right = n6
n3.right = n31
print(Solution.check_sum_tree(n26))


# Example 5
n1, n2, n3 = Node(1), Node(2), Node(3)
n3.right = n1
n1.left = n2
print(Solution.check_sum_tree(n3))
