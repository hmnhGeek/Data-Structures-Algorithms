class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _lca(root: Node, node1, node2):
        if root is None:
            return
        if root.data == node1 or root.data == node2:
            return root.data
        left = Solution._lca(root.left, node1, node2)
        right = Solution._lca(root.right, node1, node2)

        if left is None and right is None:
            return
        if left is None:
            return right
        if right is None:
            return left
        return root.data

