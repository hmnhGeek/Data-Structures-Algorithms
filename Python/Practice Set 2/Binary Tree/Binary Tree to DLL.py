class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    prev = None
    head = tail = None

    @staticmethod
    def convert_to_dll(root: Node):
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