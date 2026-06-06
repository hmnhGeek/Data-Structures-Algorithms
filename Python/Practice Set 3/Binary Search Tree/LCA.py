class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.size = self.height = self.diameter = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.diameter = 0

    def recalc_augmentation(self, parent):
        self.diameter = 0
        while parent is not None:
            left_size, left_height = 0, 0
            if parent.left is not None:
                left_size = parent.left.size
                left_height = parent.left.height
            right_size, right_height = 0, 0
            if parent.right is not None:
                right_size = parent.right.size
                right_height = parent.right.height
            parent.size = 1 + left_size + right_size
            parent.height = 1 + max(left_height, right_height)
            parent.diameter = 1 + left_height + right_height
            self.diameter = max(self.diameter, parent.diameter)
            parent = parent.parent

    def insert(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
            self.diameter = 1
            return
        self._insert(self.root, node)
        return

    def _insert(self, root, node):
        if root is None or node is None:
            return
        if node.data >= root.data:
            if root.right is not None:
                self._insert(root.right, node)
                return
            root.right = node
            node.parent = root
            self.recalc_augmentation(root)
            return
        if root.left is not None:
            self._insert(root.left, node)
            return
        root.left = node
        node.parent = root
        self.recalc_augmentation(root)
        return
