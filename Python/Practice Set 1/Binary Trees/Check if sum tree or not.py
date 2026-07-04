# Problem link - Problem link - https://www.geeksforgeeks.org/problems/sum-tree/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def is_sum_tree(root: Node):
        """
            Time complexity is O(n) and space complexity is O(h).
        """
        if root is None:
            return 0, True
        if root.left is None and root.right is None:
            return root.data, True
        left, lflag = Solution.is_sum_tree(root.left)
        right, rflag = Solution.is_sum_tree(root.right)

        if lflag and rflag:
            if left + right == root.data:
                return root.data + left + right, True
            else:
                return None, False
        return None, False


# Example 1
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n3.left = n1
n3.right = n2

print(Solution.is_sum_tree(n3)[1])


# Example 2
n10 = Node(10)
n20 = Node(20)
n30 = Node(30)
n101 = Node(10)
n102 = Node(10)

n10.left = n20
n10.right = n30
n20.left = n101
n20.right = n102

print(Solution.is_sum_tree(n10)[1])


# Example 3
a26 = Node(26)
a10 = Node(10)
a3 = Node(3)
a4 = Node(4)
a6 = Node(6)
a31 = Node(3)

a26.left = a10
a26.right = a3
a10.left = a4
a10.right = a6
a3.right = a31

print(Solution.is_sum_tree(a26)[1])


# Example 4
b26 = Node(26)
b10 = Node(10)
b3 = Node(3)
b2 = Node(2)
b6 = Node(6)
b31 = Node(3)

b26.left = b10
b26.right = b3
b10.left = b2
b10.right = b6
b3.right = b31

print(Solution.is_sum_tree(b26)[1])


# Example 5
c1 = Node(1)
c2 = Node(2)
c3 = Node(3)

c3.right = c1
c1.left = c2

print(Solution.is_sum_tree(c3)[1])
