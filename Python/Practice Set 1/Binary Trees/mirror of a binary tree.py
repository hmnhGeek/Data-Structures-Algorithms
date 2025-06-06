# Problem link - https://www.geeksforgeeks.org/create-a-mirror-tree-from-the-given-binary-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def get_mirror(root: Node):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
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

# Example 2
n12, n1, n2, n8, n9 = Node(12), Node(1), Node(2), Node(8), Node(9)
n2.left = n1
n1.left = n12
n2.right = n8
n8.right = n9
print(Solution.get_inorder(n2))
mirror2 = Solution.get_mirror(n2)
print(Solution.get_inorder(mirror2))
