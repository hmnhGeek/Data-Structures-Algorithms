class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_mirror(root: Node):
        if root is None:
            return
        left = Solution.get_mirror(root.left)
        right = Solution.get_mirror(root.right)
        root.left = right
        root.right = left
        return root

    @staticmethod
    def get_inorder(root: Node):
        inorder = []
        Solution._populate_inorder(root, inorder)
        return inorder

    @staticmethod
    def _populate_inorder(root, inorder):
        if root:
            Solution._populate_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._populate_inorder(root.right, inorder)


# Example 1
n5, n3, n6, n2, n4 = Node(5), Node(3), Node(6), Node(2), Node(4)
n5.left = n3
n5.right = n6
n3.left = n2
n3.right = n4
print(Solution.get_inorder(n5))
mirror1 = Solution.get_mirror(n5)
print(Solution.get_inorder(mirror1))
