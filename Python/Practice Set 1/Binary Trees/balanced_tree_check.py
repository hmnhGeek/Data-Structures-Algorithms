class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def check_if_balanced(root: Node) -> bool:
        status = [True]
        Solution._is_balanced(root, status)
        return status[0]

    @staticmethod
    def _is_balanced(root: Node, status):
        if root is None:
            return 0
        left_ht = Solution._is_balanced(root.left, status)
        right_ht = Solution._is_balanced(root.right, status)
        if abs(right_ht - left_ht) > 1:
            status[0] = False
        return 1 + max(left_ht, right_ht)


# Example 1
n3, n9, n20, n15, n7 = Node(3), Node(9), Node(20), Node(15), Node(7)
n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7
print(Solution.check_if_balanced(n3))

# Example 2
n1, n2, n3, n4, n5, n6, n7 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
n1.left = n3
n3.left = n5
n3.right = n4
n5.left = n7
n5.right = n6
n1.right = n2
print(Solution.check_if_balanced(n1))


# Example 3
n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
n1.left = n2
n2.left = n4
n2.right = n5
n1.right = n3
print(Solution.check_if_balanced(n1))


# Example 4
n1, n2, n3, n4, n5, n6, n7, n8, n9 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9)
n1.left = n2
n2.left = n4
n2.right = n5
n5.left = n8
n1.right = n3
n3.left = n6
n3.right = n9
n6.right = n7
print(Solution.check_if_balanced(n1))
