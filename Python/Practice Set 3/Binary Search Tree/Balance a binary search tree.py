class Node:
    def __init__(self, data):
        self.data = data
        self.height = self.size = self.diameter = 1
        self.left = self.right = self.parent = None


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
            self.diameter = max(self.diameter, parent.size)
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
        node = self.get_node(self.root, x)
        return self._delete(node)

    def get_node(self, start, x):
        if start is None or x is None:
            return
        if start.data == x:
            return start
        if x >= start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, height = {start.height}, diameter = {start.diameter}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def balance_bst(bst: BinarySearchTree):
        balanced_bst = BinarySearchTree()
        inorder = []
        Solution._get_inorder(bst.root, inorder)
        Solution._insert_into_balanced_bst(balanced_bst, inorder, 0, len(inorder) - 1)
        return balanced_bst

    @staticmethod
    def _get_inorder(root, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def _insert_into_balanced_bst(balanced_bst, inorder, low, high):
        if low > high:
            return
        mid = int(low + (high - low)/2)
        balanced_bst.insert(inorder[mid])
        Solution._insert_into_balanced_bst(balanced_bst, inorder, low, mid - 1)
        Solution._insert_into_balanced_bst(balanced_bst, inorder, mid + 1, high)


bst1 = BinarySearchTree()
for i in [30, 20, 10]:
    bst1.insert(i)
bst1.show()
bbst1 = Solution.balance_bst(bst1)
bbst1.show()

bst2 = BinarySearchTree()
for i in [4, 3, 5, 2, 6, 1, 7]:
    bst2.insert(i)
bst2.show()
bbst2 = Solution.balance_bst(bst2)
bbst2.show()