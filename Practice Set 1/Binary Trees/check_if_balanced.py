from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _check_balanced(root: Node, balanced_status: List[bool]) -> int:
        if root is None:
            return 0
        left_ht = Solution._check_balanced(root.left, balanced_status)
        right_ht = Solution._check_balanced(root.right, balanced_status)
        if abs(left_ht - right_ht) > 1:
            balanced_status[0] = False
        return 1 + max(left_ht, right_ht)

    @staticmethod
    def check_if_balanced(root: Node) -> bool:
        balanced_status = [True]
        Solution._check_balanced(root, balanced_status)
        return balanced_status[0]


# Example 1
n10, n20, n30, n40, n50 = Node(10), Node(20), Node(30), Node(40), Node(50)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n50
print(Solution.check_if_balanced(n10))


# Example 2
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n2.right = n3
print(Solution.check_if_balanced(n1))


# Example 3
n1, n2, n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
n1.left = n2
n1.right = n3
n2.left = n4
n4.left = n5
print(Solution.check_if_balanced(n1))