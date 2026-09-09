# Problem link - https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/


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
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, height = {start.height}, diameter = {start.diameter}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def merge_bsts(bst1: BinarySearchTree, bst2: BinarySearchTree) -> BinarySearchTree:
        """
            Time complexity is O(n + m) and space complexity is O(n + m).
        """

        # This takes O(n) time and O(log(n)) space.
        inorder1 = []
        Solution._get_inorder(bst1.root, inorder1)

        # This takes O(m) time and O(log(m)) space.
        inorder2 = []
        Solution._get_inorder(bst2.root, inorder2)

        # This takes O(n + m) time and O(n + m) space.
        inorder = Solution._merge(inorder1, inorder2)

        # This takes O(log(n + m)) time and O(n + m) space.
        return Solution._construct_balanced_bst(inorder)

    @staticmethod
    def _get_inorder(root: Node, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def _merge(left, right):
        i, j = 0, 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    @staticmethod
    def _construct_balanced_bst(inorder) -> BinarySearchTree:
        bst = BinarySearchTree()
        n = len(inorder)
        Solution._balanced_insert(bst, inorder, 0, n - 1)
        return bst

    @staticmethod
    def _balanced_insert(bst, inorder, low, high):
        if low > high:
            return
        mid = int(low + (high - low)/2)
        bst.insert(inorder[mid])
        Solution._balanced_insert(bst, inorder, low, mid - 1)
        Solution._balanced_insert(bst, inorder, mid + 1, high)


def example1():
    t1 = BinarySearchTree()
    t1.insert(3)
    t1.insert(1)
    t1.insert(5)

    t2 = BinarySearchTree()
    t2.insert(4)
    t2.insert(2)
    t2.insert(6)

    mt = Solution.merge_bsts(t1, t2)
    mt.show()


def example2():
    t1 = BinarySearchTree()
    t1.insert(5)
    t1.insert(3)
    t1.insert(0)

    t2 = BinarySearchTree()
    t2.insert(8)
    t2.insert(2)
    t2.insert(1)
    t2.insert(10)

    merged = Solution.merge_bsts(t1, t2)
    merged.show()


def example3():
    t1 = BinarySearchTree()
    t1.insert(3)
    t1.insert(2)
    t1.insert(1)
    t1.insert(5)

    t2 = BinarySearchTree()
    t2.insert(4)
    t2.insert(1)
    t2.insert(2)
    t2.insert(7)
    t2.insert(9)

    merged = Solution.merge_bsts(t2, t1)
    merged.show()


def example4():
    t1 = BinarySearchTree()
    t1.insert(2)
    t1.insert(1)
    t1.insert(3)

    t2 = BinarySearchTree()
    t2.insert(4)

    merged = Solution.merge_bsts(t1, t2)
    merged.show()


example1()
print()
example2()
print()
example3()
print()
example4()
print()
