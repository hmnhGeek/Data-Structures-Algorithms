# Problem link - https://www.geeksforgeeks.org/problems/predecessor-and-successor/1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.height = self.size = self.diameter = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.diameter = 0

    def recalc_augmentation(self, parent):
        self.diameter = 0
        while parent is not None:
            left_size = parent.left.size if parent.left is not None else 0
            left_height = parent.left.height if parent.left is not None else 0
            right_size = parent.right.size if parent.right is not None else 0
            right_height = parent.right.height if parent.right is not None else 0
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
            parent = parent.parent
            node = node.parent
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
            parent = parent.parent
            node = node.parent
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
                self.diameter = 0
            del node
            self.recalc_augmentation(parent)
            return
        if node.right is not None:
            successor = self.get_successor(node)
            successor.data, node.data = node.data, successor.data
            self._delete(successor)
            return
        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        self._delete(predecessor)
        return

    def delete(self, x):
        node = self.get_node(self.root, x)
        self._delete(node)

    def get_node(self, start, x):
        if start is None or x is None:
            return
        if start.data == x:
            return start
        if x > start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.height}, d = {start.diameter}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def get_predecessor_and_successor(arr, x):
        """
            Time complexity is O(log(n)) and space complexity is O(log(n)).
        """
        bst = Solution.get_bst(arr)
        node = bst.get_node(bst.root, x)
        if node is None:
            bst.insert(x)
            nd = bst.get_node(bst.root, x)
            predecessor = bst.get_predecessor(nd)
            successor = bst.get_successor(nd)
            p = predecessor.data if predecessor is not None else None
            s = successor.data if successor is not None else None
            bst.delete(x)
            return [p, s]
        predecessor = bst.get_predecessor(node)
        successor = bst.get_successor(node)
        p = predecessor.data if predecessor is not None else None
        s = successor.data if successor is not None else None
        return [p, s]

    @staticmethod
    def get_bst(arr):
        bst = BinarySearchTree()
        for i in arr:
            bst.insert(i)
        return bst


print(Solution.get_predecessor_and_successor([50, 30, 70, 20, 40, 60, 80], 65))
print(Solution.get_predecessor_and_successor([8, 1, 9, 4, 10, 3], 8))
