class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.data = data
        self.right = None
        self.size = 1
        self.d = 1
        self.ht = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

    def recalc_augmentation(self, parent):
        self.d = 0
        while parent is not None:
            left_sz, right_sz = parent.left.size if parent.left else 0, parent.right.size if parent.right else 0
            left_ht, right_ht = parent.left.ht if parent.left else 0, parent.right.ht if parent.right else 0

            parent.size = 1 + left_sz + right_sz
            parent.ht = 1 + max(left_ht, right_ht)
            parent.d = 1 + left_ht + right_ht
            self.d = max(self.d, parent.d)
            parent = parent.parent

    def _insert(self, start, node):
        if node is None or start is None:
            return

        if node.data >= start.data:
            if start.right is not None:
                return self._insert(start.right, node)
            start.right = node
            node.parent = start
            self.recalc_augmentation(start)
            return

        if start.left is not None:
            return self._insert(start.left, node)
        start.left = node
        node.parent = start
        self.recalc_augmentation(start)
        return

    def insert(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
            self.d = 1
            return
        return self._insert(self.root, node)

    def _get_inorder(self, start, inorder):
        if start:
            self._get_inorder(start.left, inorder)
            inorder.append(start)
            self._get_inorder(start.right, inorder)

    def get_inorder(self):
        inorder = []
        self._get_inorder(self.root, inorder)
        return inorder

    def _get_preorder(self, start, preorder):
        if start:
            preorder.append(start)
            self._get_preorder(start.left, preorder)
            self._get_preorder(start.right, preorder)

    def get_preorder(self):
        preorder = []
        self._get_preorder(self.root, preorder)
        return preorder

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)

