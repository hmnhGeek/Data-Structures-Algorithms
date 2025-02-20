# Problem link - https://www.geeksforgeeks.org/problems/transform-to-sum-tree/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def convert(root: Node):
        """
            Overall time complexity is O(n) and space complexity is O(h).
        """

        # if the root node is None, return 0 sum.
        if root is None:
            return 0

        # if it's a leaf node
        if root.left is None and root.right is None:
            temp = root.data
            # assign its data to be 0.
            root.data = 0
            # return previous data + 0
            return temp + root.data

        # compute sum from left subtree
        left_val = Solution.convert(root.left)
        # compute sum from right subtree
        right_val = Solution.convert(root.right)
        # store the current root data in temp
        temp = root.data
        # reassign root's data to be left subtree sum + right subtree sum
        root.data = left_val + right_val
        # and return temp + current root data
        return temp + root.data

    @staticmethod
    def _show(root: Node):
        if root:
            Solution._show(root.left)
            print(root.data, end=" ")
            Solution._show(root.right)

    @staticmethod
    def show(root: Node):
        Solution._show(root)
        print()


# Example 1
n10, n2, n6, n8, n4, n7, n5 = Node(10), Node(-2), Node(6), Node(8), Node(-4), Node(7), Node(5)
n10.left = n2
n2.left = n8
n6.left = n7
n2.right = n4
n10.right = n6
n6.right = n5
Solution.show(n10)
Solution.convert(n10)
Solution.show(n10)

# Example 2
n5, n1, n8, n4, n6 = Node(5), Node(1), Node(-8), Node(4), Node(6)
n5.right = n1
n1.left = n8
n1.right = n4
n8.left = n6
Solution.show(n5)
Solution.convert(n5)
Solution.show(n5)

# Example 3
n1, n11, n2, n3, n111 = Node(1), Node(1), Node(-2), Node(3), Node(1)
n1.left = n2
n1.right = n11
n2.left = n3
n2.right = n111
Solution.show(n1)
Solution.convert(n1)
Solution.show(n1)