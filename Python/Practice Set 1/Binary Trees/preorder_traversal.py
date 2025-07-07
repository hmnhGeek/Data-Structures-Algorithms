class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _preorder(root, preorder):
        if root:
            preorder.append(root.data)
            Solution._preorder(root.left, preorder)
            Solution._preorder(root.right, preorder)

    @staticmethod
    def preorder_recursive(root):
        preorder = []
        Solution._preorder(root, preorder)
        return preorder