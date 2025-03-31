# Problem link - https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1


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
            node.data, successor.data = successor.data, node.data
            return self._delete(successor)
        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        return self._delete(predecessor)

    def get_node(self, start, x):
        if start is None or x is None:
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
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def _lca(root, x, y):
        # if a null node is encountered, return nothing
        if root is None:
            return None

        # if the root's data matches with either x or y, return root's data.
        if root.data == x or root.data == y:
            return root.data

        # recursively check for LCA in left and right subtrees.
        left = Solution._lca(root.left, x, y)
        right = Solution._lca(root.right, x, y)

        # if x and y are not found in the subtrees of root, return nothing.
        if left is None and right is None:
            return None

        # if x or y or both are found in right subtree, return right.
        if left is None:
            return right

        # if x or y or both are found in left subtree, return left.
        if right is None:
            return left

        # if x and y are found in both subtrees, return root's data as root will be the LCA.
        return root.data

    @staticmethod
    def get_lca(bst: BinarySearchTree, x, y):
        """
            Time complexity is O(n) and space complexity is O(log(n)).
        """

        lca = Solution._lca(bst.root, x, y)
        return lca


# Example 1
bst1 = BinarySearchTree()
for i in [5, 4, 6, 3, 7, 8]:
    bst1.insert(i)
print(Solution.get_lca(bst1, 7, 8))

# Example 2
bst2 = BinarySearchTree()
for i in [20, 8, 22, 4, 12, 10, 14]:
    bst2.insert(i)
print(Solution.get_lca(bst2, 8, 14))

# Example 3
bst3 = BinarySearchTree()
for i in [2, 1, 3]:
    bst3.insert(i)
print(Solution.get_lca(bst3, 1, 3))

# Example 4
t1 = BinarySearchTree()
for i in [5, 4, 6, 3, 7, 8]:
    t1.insert(i)
print(Solution.get_lca(t1, 7, 8))
print(Solution.get_lca(t1, 7, 3))
print(Solution.get_lca(t1, 4, 4))

# Example 5
t2 = BinarySearchTree()
for i in [2, 1, 3]:
    t2.insert(i)
print(Solution.get_lca(t2, 1, 3))
print(Solution.get_lca(t2, 1, 7))
print(Solution.get_lca(t2, 9, 7))

# Example 6
t3 = BinarySearchTree()
for i in [6, 2, 8, 0, 4, 7, 9, 3, 5]:
    t3.insert(i)
print(Solution.get_lca(t3, 2, 8))
print(Solution.get_lca(t3, 2, 4))
