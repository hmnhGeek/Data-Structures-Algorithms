class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_max_path_sum(root: Node):
        if root is None:
            return 0, 0
        left_ht, left_sum = Solution.get_max_path_sum(root.left)
        right_ht, right_sum = Solution.get_max_path_sum(root.right)
        if left_ht > right_ht:
            return 1 + left_ht, left_sum + root.data
        elif right_ht > left_ht:
            return 1 + right_ht, right_sum + root.data
        else:
            return 1 + left_ht, max(left_sum, right_sum) + root.data


# Example 1
n1, n2, n3, n4, n5, n6, n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
print(Solution.get_max_path_sum(n1))


# Example 2
n1, n2, n3, n4, n5, n6, n7, n21 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(2)
n4.left = n2
n4.right = n5
n2.left = n7
n2.right = n1
n1.left = n6
n5.left = n21
n5.right = n3
print(Solution.get_max_path_sum(n4))


# Example 3
n10, n5, n15, n3, n7, n20, n1 = Node(10), Node(5), Node(15), Node(3), Node(7), Node(20), Node(1)
n10.left = n5
n10.right = n15
n5.left = n3
n5.right = n7
n3.left = n1
n15.right = n20
print(Solution.get_max_path_sum(n10))

# Example 4
print(Solution.get_max_path_sum(None))
