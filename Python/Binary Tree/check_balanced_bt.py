# Video - https://www.youtube.com/watch?v=Yt50Jfbd8Po&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=16


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BalancedStatus:
    def __init__(self, is_balanced):
        self._is_balanced = is_balanced

    def set_is_balanced(self, value):
        self._is_balanced = value

    def get_is_balanced(self):
        return self._is_balanced


class Solution:
    @staticmethod
    def _update_heights(root: Node, balanced_object: BalancedStatus):
        # if the node is null, return 0 height.
        if root is None:
            return 0

        # get left and right height from the subtrees.
        left_ht = Solution._update_heights(root.left, balanced_object)
        right_ht = Solution._update_heights(root.right, balanced_object)

        # if the difference in heights is more than 1, set balanced object to false, implying that the
        # tree is not balanced.
        if abs(left_ht - right_ht) > 1:
            balanced_object.set_is_balanced(False)

        # continue with same evaluation of the height at root node.
        height_at_root = 1 + max(left_ht, right_ht)
        return height_at_root

    @staticmethod
    def check_if_balanced(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # initialize an object which stores the current status of the binary tree being balanced as True.
        # Since in Python, objects are passed by reference, we can set its value any time in the recursion.
        balance_object = BalancedStatus(True)
        # calculate the height of each node in O(n) time and O(n) space.
        Solution._update_heights(root, balance_object)
        # return the balanced status of the binary tree.
        return balance_object.get_is_balanced()


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