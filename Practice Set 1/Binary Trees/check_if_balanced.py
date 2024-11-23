# Problem link - https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1


from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _check_balanced(root: Node, balanced_status: List[bool]) -> int:
        """
            Time complexity is O(n) and space complexity is O(h).
        """

        # if there is no node, then the height is 0.
        if root is None:
            return 0
        # get the left and right height of the root.
        left_ht = Solution._check_balanced(root.left, balanced_status)
        right_ht = Solution._check_balanced(root.right, balanced_status)
        # if the height differences is greater than 1, the tree is not balanced, mark it as un-balanced.
        if abs(left_ht - right_ht) > 1:
            balanced_status[0] = False
        # return the height at root node to complete the recursion.
        return 1 + max(left_ht, right_ht)

    @staticmethod
    def check_if_balanced(root: Node) -> bool:
        """
            Time complexity is O(n) and space complexity is O(h).
        """

        # storing a variable to hold the balanced status of the tree.
        balanced_status = [True]
        # recursively call the height method for each node and simultaneously check for the balanced status.
        Solution._check_balanced(root, balanced_status)
        # return the balanced status after it getting updated from the recursive call.
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


# Example 4
n1, n21, n22, n31, n32, n41, n42 = Node(1), Node(2), Node(2), Node(3), Node(3), Node(4), Node(4)
n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n32
n31.left = n41
n31.right = n42
print(Solution.check_if_balanced(n1))


# Example 5
n3, n9, n20, n15, n7 = Node(3), Node(9), Node(20), Node(15), Node(7)
n3.left = n9
n3.right = n20
n20.left = n15
n20.right = n7
print(Solution.check_if_balanced(n3))


# Example 6
print(Solution.check_if_balanced(None))