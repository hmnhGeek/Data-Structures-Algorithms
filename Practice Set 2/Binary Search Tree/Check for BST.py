# Problem link - https://www.geeksforgeeks.org/problems/check-for-bst/1
# Solution - https://www.youtube.com/watch?v=f-sj7I5oXEI


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _check(root: Node, low, high):
        # a null node is always a BST.
        if root is None:
            return True

        # if the root node does not lie in the low, high range, return False.
        if not (low < root.data < high):
            return False

        # recursively check for left and right subtrees.
        left = Solution._check(root.left, low, root.data)
        right = Solution._check(root.right, root.data, high)

        # return true only if both subtrees return true.
        return left and right

    @staticmethod
    def is_bst(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """

        # pass the root node of the tree with range -inf to inf.
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
