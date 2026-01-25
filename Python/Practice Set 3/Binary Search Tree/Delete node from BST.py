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
            left_ht = parent.left.height if parent.left else 0
            left_sz = parent.left.size if parent.left else 0
            right_ht = parent.right.height if parent.right else 0
            right_sz = parent.right.size if parent.right else 0
            parent.size = 1 + left_sz + right_sz
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
        return
