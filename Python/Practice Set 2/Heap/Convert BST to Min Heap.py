# Problem link - https://www.geeksforgeeks.org/convert-bst-min-heap/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.size = self.height = self.d = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

    def recalc_aug(self, parent):
        self.d = 0
        while parent is not None:
            left_size, right_size = parent.left.size if parent.left is not None else 0, parent.right.size if parent.right is not None else 0
            left_ht, right_ht = parent.left.height if parent.left is not None else 0, parent.right.height if parent.right is not None else 0
            parent.size = 1 + left_size + right_size
            parent.height = 1 + max(left_ht, right_ht)
            parent.d = 1 + left_ht + right_ht
            self.d = max(self.d, parent.d)
            parent = parent.parent

    def insert(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
            self.d = 1
            return
        self._insert(self.root, node)

    def _insert(self, start, node):
        if start is None or node is None:
            return
        if node.data >= start.data:
            if start.right is not None:
                self._insert(start.right, node)
                return
            start.right = node
            node.parent = start
            self.recalc_aug(start)
            return
        if start.left is not None:
            self._insert(start.left, node)
            return
        start.left = node
        node.parent = start
        self.recalc_aug(start)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, height = {start.height}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def convert_to_min_heap(bst: BinarySearchTree):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        preorder = []
        Solution._get_preorder(bst.root, preorder)
        inorder = []
        Solution._get_inorder(bst.root, inorder)
        for i in range(len(inorder)):
            preorder[i].data = inorder[i]

    @staticmethod
    def _get_preorder(root, preorder):
        if root:
            preorder.append(root)
            Solution._get_preorder(root.left, preorder)
            Solution._get_preorder(root.right, preorder)

    @staticmethod
    def _get_inorder(root, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def test(*args):
        bst = BinarySearchTree()
        for i in args:
            bst.insert(i)
        bst.show()
        Solution.convert_to_min_heap(bst)
        bst.show()


# Example 1
Solution.test(4, 2, 6, 1, 3, 5, 7)

# Example 2
Solution.test(6, 4, 8, 1, 5, 7, 10)
