class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _check_sum_tree(root: Node):
        if root is None:
            return 0, True
        if root.left is None and root.right is None:
            return root.data, True

        left_ans, left_sum_tree = Solution._check_sum_tree(root.left)
        right_ans, right_sum_tree = Solution._check_sum_tree(root.right)
        if left_sum_tree and right_sum_tree:
            _sum = root.data + left_ans + right_ans
            if root.data == left_ans + right_ans:
                return _sum, True
            else:
                return _sum, False
        else:
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
