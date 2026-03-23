# Problem link - https://www.geeksforgeeks.org/problems/binary-tree-to-dll/1
# Solution - https://www.youtube.com/watch?v=nGNoTdav5bQ


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    prev = None
    head = tail = None

    @staticmethod
    def convert_to_dll(root: Node):
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        Solution.prev = Solution.head = Solution.tail = None
        Solution._solve(root)
        curr = Solution.head
        while curr.right is not None:
            curr = curr.right
        Solution.tail = curr

    @staticmethod
    def _solve(root: Node):
        if root is None:
            return
        Solution._solve(root.left)
        if Solution.prev is None:
            Solution.head = root
        else:
            root.left = Solution.prev
            Solution.prev.right = root
        Solution.prev = root
        Solution._solve(root.right)


# Example 1
n10, n12, n15, n25, n30, n36 = Node(10), Node(12), Node(15), Node(25), Node(30), Node(36)
n10.left = n12
n10.right = n15
n12.left = n25
n12.right = n30
n15.left = n36
Solution.convert_to_dll(n10)
curr = n25
while curr is not None:
    print(curr.data, end=" ")
    curr = curr.right
print()

# Example 2
n10, n20, n30, n40, n60 = Node(10), Node(20), Node(30), Node(40), Node(60)
n10.left = n20
n10.right = n30
n20.left = n40
n20.right = n60
Solution.convert_to_dll(n10)
curr = n40
while curr is not None:
    print(curr.data, end=" ")
    curr = curr.right
print()

# Example 3
n1, n2, n3 = Node(1), Node(2), Node(3)
n1.left = n2
n1.right = n3
Solution.convert_to_dll(n1)
curr = n2
while curr is not None:
    print(curr.data, end=" ")
    curr = curr.right
print()
