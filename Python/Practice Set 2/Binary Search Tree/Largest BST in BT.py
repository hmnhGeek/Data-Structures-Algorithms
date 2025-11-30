# Problem link - https://www.geeksforgeeks.org/problems/largest-bst/1
# Solution - https://www.youtube.com/watch?v=X0oXMdtUDwo


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Element:
    def __init__(self, maxi, mini, size):
        self.maxi = maxi
        self.mini = mini
        self.size = size


class Solution:
    @staticmethod
    def get_largest_bst(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        if root is None:
            return Element(-1e6, 1e6, 0)
        left = Solution.get_largest_bst(root.left)
        right = Solution.get_largest_bst(root.right)
        if left.maxi <= root.data <= right.mini:
            return Element(
                max(right.maxi, root.data),
                min(left.mini, root.data),
                1 + left.size + right.size
            )
        return Element(1e6, -1e6, max(left.size, right.size))


# Example 1
n20, n15, n40, n14, n18, n30, n60, n17, n16, n19, n50 = Node(20), Node(15), Node(40), Node(14), Node(18), Node(30), Node(60), Node(17), Node(16), Node(19), Node(50)
n20.left = n15
n15.left = n14
n18.left = n16
n40.left = n30
n60.left = n50
n20.right = n40
n40.right = n60
n15.right = n18
n18.right = n19
n14.right = n17
print(Solution.get_largest_bst(n20).size)


# Example 2
n10 = Node(10)
n5 = Node(5)
n15 = Node(15)
n1 = Node(1)
n8 = Node(8)
n7 = Node(7)
n10.left = n5
n5.left = n1
n5.right = n8
n10.right = n15
n15.right = n7
print(Solution.get_largest_bst(n10).size)
