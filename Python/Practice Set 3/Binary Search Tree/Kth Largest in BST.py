class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.height = self.diameter = self.size = 1


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
            return self._delete(successor)
        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        return self._delete(predecessor)

    def delete(self, x):
        node = self._get_node(self.root, x)
        self._delete(node)

    def _get_node(self, start, x):
        if start is None or x is None:
            return
        if start.data == x:
            return start
        if x > start.data:
            return self._get_node(start.right, x)
        return self._get_node(start.left, x)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if self.root == start else ''}, size = {start.size}, ht = {start.height}, d = {start.diameter}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def get_kth_largest(bst: BinarySearchTree, k: int, n: int):
        counter = [0, None]
        Solution._solve(bst.root, counter, n - k + 1)
        return counter[1].data if counter[1] is not None else None

    @staticmethod
    def _solve(start, counter, k):
        if start:
            Solution._solve(start.left, counter, k)
            counter[0] += 1
            if counter[0] == k:
                counter[1] = start
            Solution._solve(start.right, counter, k)


# Example 1
bst = BinarySearchTree()
for i in [4, 2, 9]:
    bst.insert(i)
print(Solution.get_kth_largest(bst, 2, 3))

# Example 2
bst = BinarySearchTree()
for i in [9, 10]:
    bst.insert(i)
print(Solution.get_kth_largest(bst, 1, 2))

# Example 3
bst = BinarySearchTree()
for i in [6, 2, 7, 3, 4, 9]:
    bst.insert(i)
print(Solution.get_kth_largest(bst, 5, 6))
