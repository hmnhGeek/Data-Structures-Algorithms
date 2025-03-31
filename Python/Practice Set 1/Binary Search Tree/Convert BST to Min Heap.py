# Problem link - https://www.geeksforgeeks.org/convert-bst-min-heap/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.size = self.ht = self.d = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

    def recalc_aug(self, parent):
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
        if start is None or node is None:
            return
        if node.data >= start.data:
            if start.right is not None:
                return self._insert(start.right, node)
            start.right = node
            node.parent = start
            self.recalc_aug(start)
            return
        if start.left is not None:
            return self._insert(start.left, node)
        start.left = node
        node.parent = start
        self.recalc_aug(start)
        return

    def insert(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
            self.d = 1
            return
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
        if node.right is not None:
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
        if start is None or x is None:
            return
        if start.data == x:
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
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def _get_inorder(root, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def _get_preorder(root, preorder):
        if root:
            preorder.append(root)
            Solution._get_preorder(root.left, preorder)
            Solution._get_preorder(root.right, preorder)

    @staticmethod
    def convert_to_min_heap(bst: BinarySearchTree):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # time complexity to get inorder is O(n) and space complexity is O(n).
        inorder = []
        Solution._get_inorder(bst.root, inorder)

        # time complexity to get preorder is O(n) and space complexity is O(n).
        preorder = []
        Solution._get_preorder(bst.root, preorder)

        # this will take additional O(n) and O(n) space.
        n = len(inorder)
        for i in range(n):
            preorder[i].data = inorder[i]


# Example 1
t1 = BinarySearchTree()
for i in [4, 2, 6, 1, 3, 5, 7]:
    t1.insert(i)
t1.show()
Solution.convert_to_min_heap(t1)
t1.show()
