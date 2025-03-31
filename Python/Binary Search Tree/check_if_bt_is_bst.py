# Problem link - https://www.geeksforgeeks.org/problems/check-for-bst/1
# Solution - https://www.youtube.com/watch?v=f-sj7I5oXEI


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _check(root: Node, low, high):
        # if the node is a leaf node, simply check if it is in the desired range or not.
        if root.left is None and root.right is None:
            return low < root.data < high

        # if the current node is not a leaf node, and is in correct range...
        if low < root.data < high:
            # assume left subtree is a BST.
            left = True
            if root.left is not None:
                # find if it is truly a BST by changing the range to (low, root.data).
                left = Solution._check(root.left, low, root.data)

            # assume right subtree is a BST.
            right = True
            if root.right is not None:
                # find if it is truly a BST by changing the range to (root.data, high).
                right = Solution._check(root.right, root.data, high)

            # return true at current node if both subtrees are BST, else return False.
            return left and right
        else:
            # if the current node is not in the correct range, return False.
            return False

    @staticmethod
    def is_bst(root: Node):
        """
            Time complexity is O(n) and space complexity is O(H).
        """

        # if you've an empty tree, return True as it is a BST.
        if root is None:
            return True

        # pass -inf to inf range for root node in the _check recursive method.
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