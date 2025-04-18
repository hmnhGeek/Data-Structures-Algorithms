class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def show_tree(root: Node):
        Solution._show(root)
        print()

    @staticmethod
    def _show(root: Node):
        if root:
            Solution._show(root.left)
            print(root.data, end=" ")
            Solution._show(root.right)

    @staticmethod
    def convert_to_bst(root: Node):
        inorder = []
        Solution._get_inorder(root, inorder)
        sorted_inorder = [i.data for i in inorder]
        sorted_inorder.sort()
        for i in range(len(inorder)):
            inorder[i].data = sorted_inorder[i]

    @staticmethod
    def _get_inorder(root: Node, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root)
            Solution._get_inorder(root.right, inorder)
