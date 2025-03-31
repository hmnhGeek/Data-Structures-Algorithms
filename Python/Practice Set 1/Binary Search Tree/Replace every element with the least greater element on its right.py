# Problem link - https://www.geeksforgeeks.org/replace-every-element-with-the-least-greater-element-on-its-right/


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.size = self.ht = self.d = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

    def recalc_aug(self, parent):
        self.d = 0
        while parent is not None:
            left_ht, right_ht = parent.left.ht if parent.left else 0, parent.right.ht if parent.right else 0
            left_sz, right_sz = parent.left.size if parent.left else 0, parent.right.size if parent.right else 0
            parent.size = 1 + left_sz + right_sz
            parent.ht = 1 + max(left_ht, right_ht)
            parent.d = 1 + left_ht + right_ht
            self.d = max(self.d, parent.d)
            parent = parent.parent

    def _insert(self, start, node):
        if start is None or node is None:
            return
        if node.data >= start.data:
            if start.right is not None:
                return self._insert(start.right, node)
            start.right = node
            node.parent = start
            self.recalc_aug(start)
            return node
        if start.left is not None:
            return self._insert(start.left, node)
        start.left = node
        node.parent = start
        self.recalc_aug(start)
        return node

    def insert(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
            self.d = 1
            return node
        return self._insert(self.root, node)

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
            self.recalc_aug(parent)
            return
        if node.right is not None:
            successor = self.get_successor(node)
            successor.data, node.data = node.data, successor.data
            return self._delete(successor)
        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        return self._delete(predecessor)

    def get_node(self, start, x):
        if x is None or start is None:
            return
        if x == start.data:
            return start
        if x > start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def delete(self, x):
        node = self.get_node(self.root, x)
        if node is not None:
            return self._delete(node)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(
                f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def replace(arr):
        """
            Time complexity is O(n * log(n)) and space complexity is O(n).
        """

        n = len(arr)

        # create a result array of size n with all -1s.
        result = [-1] * n

        # create a BST which will hold all the n-elements, hence O(n) space.
        bst = BinarySearchTree()

        # traverse from the end of the array in n iterations.
        for i in range(n - 1, -1, -1):
            # insert the ith element in BST in log(n) time.
            node = bst.insert(arr[i])
            # get the successor of this inserted node in log(n) time.
            successor = bst.get_successor(node)
            # if successor is found, replace result[i] with it.
            if successor is not None:
                result[i] = successor.data

        # finally return the result array.
        return result


print(Solution.replace([8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]))
print(Solution.replace([17, 18, 5, 4, 6, 1]))
print(Solution.replace([400]))
print(Solution.replace([1, 4, 2, 6]))
