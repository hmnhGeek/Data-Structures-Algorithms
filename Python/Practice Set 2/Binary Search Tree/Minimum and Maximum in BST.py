# Problem link - https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.size = self.height = self.d = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

    def recalc_augmentation(self, parent):
        self.d = 0
        while parent is not None:
            left_size, right_size = parent.left.size if parent.left else 0, parent.right.size if parent.right else 0
            left_ht, right_ht = parent.left.height if parent.left else 0, parent.right.height if parent.right else 0
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
            self.recalc_augmentation(start)
            return
        if start.left is not None:
            self._insert(start.left, node)
            return
        start.left = node
        node.parent = start
        self.recalc_augmentation(start)
        return

    def get_leftmost_leaf(self, node):
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node

    def get_rightmost_leaf(self, node):
        if node is None:
            return
        while node.right is not None:
            node = node.right
        return node

    def get_successor(self, node):
        if node is None:
            return
        if node.right is not None:
            return self.get_leftmost_leaf(node.right)
        parent = node.parent
        if parent is None:
            return
        while parent.left != node:
            node = node.parent
            parent = parent.parent
            if parent is None:
                return
        return parent

    def get_predecessor(self, node):
        if node is None:
            return
        if node.left is not None:
            return self.get_rightmost_leaf(node.left)
        parent = node.parent
        if parent is None:
            return
        while parent.right != node:
            node = node.parent
            parent = parent.parent
            if parent is None:
                return
        return parent

    def _delete(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            parent = node.parent
            if parent is not None:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
                self.d = 0
            del node
            self.recalc_augmentation(parent)
            return
        if node.right is not None:
            successor = self.get_successor(node)
            successor.data, node.data = node.data, successor.data
            return self._delete(successor)
        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        return self._delete(predecessor)

    def delete(self, x):
        node = self._get_node(self.root, x)
        self._delete(node)

    def _get_node(self, root, x):
        if root is None or x is None:
            return
        if x == root.data:
            return root
        if x > root.data:
            return self._get_node(root.right, x)
        return self._get_node(root.left, x)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.height}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()

    def get_min_max(self):
        if self.root is None:
            return None, None
        return self.get_leftmost_leaf(self.root).data, self.get_rightmost_leaf(self.root).data


class Solution:
    @staticmethod
    def get_min_max(*args):
        """
            Time complexity is O(log(n)) and space complexity is O(n).
        """
        bst = BinarySearchTree()
        for i in args:
            bst.insert(i)
        return bst.get_min_max()


print(Solution.get_min_max(5, 4, 6, 3, 7, 1))
print(Solution.get_min_max(10, 5, 20, 2))
