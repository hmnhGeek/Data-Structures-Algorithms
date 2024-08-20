# Problem link - https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/


class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.data = data
        self.right = None
        self.size = 1
        self.ht = 1
        self.d = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

    def recalc_aug(self, parent):
        self.d = 0
        while parent is not None:
            left_size = parent.left.size if parent.left else 0
            right_size = parent.right.size if parent.right else 0

            left_ht = parent.left.ht if parent.left else 0
            right_ht = parent.right.ht if parent.right else 0

            parent.size = 1 + left_size + right_size
            parent.ht = 1 + max(left_ht, right_ht)
            parent.d = 1 + left_ht + right_ht
            self.d = max(parent.d, self.d)

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
            successor.data, node.data = node.data, successor.data
            return self._delete(successor)

        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        return self._delete(predecessor)

    def get_node(self, start, data):
        if start is None or data is None:
            return

        if start.data == data:
            return start
        if data >= start.data:
            return self.get_node(start.right, data)
        return self.get_node(start.left, data)

    def delete(self, x):
        node = self.get_node(self.root, x)
        if node is not None:
            return self._delete(node)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Node = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)

    def _get_inorder(self, start, inorder):
        if start:
            self._get_inorder(start.left, inorder)
            inorder.append(start.data)
            self._get_inorder(start.right, inorder)

    def get_inorder(self):
        inorder = []
        self._get_inorder(self.root, inorder)
        return inorder


def merge_inorder_traversals(inorder1, inorder2):
    i, j = 0, 0
    merged = []

    while i < len(inorder1) and j < len(inorder2):
        if inorder1[i] <= inorder2[j]:
            merged.append(inorder1[i])
            i += 1
        else:
            merged.append(inorder2[j])
            j += 1

    while i < len(inorder1):
        merged.append(inorder1[i])
        i += 1

    while j < len(inorder2):
        merged.append(inorder2[j])
        j += 1

    return merged


def construct_tree(tree: BinarySearchTree, low: int, high: int, inorder):
    if low > high:
        return

    mid = int(low + (high - low)/2)
    tree.insert(inorder[mid])
    construct_tree(tree, low, mid - 1, inorder)
    construct_tree(tree, mid + 1, high, inorder)


def merge_bst(bst1: BinarySearchTree, bst2: BinarySearchTree):
    inorder1 = bst1.get_inorder()
    inorder2 = bst2.get_inorder()

    # merge the inorder lists
    inorder = merge_inorder_traversals(inorder1, inorder2)

    merged_tree = BinarySearchTree()
    construct_tree(merged_tree, 0, len(inorder) - 1, inorder)
    return merged_tree


def example1():
    t1 = BinarySearchTree()
    t1.insert(3)
    t1.insert(1)
    t1.insert(5)

    t2 = BinarySearchTree()
    t2.insert(4)
    t2.insert(2)
    t2.insert(6)

    mt = merge_bst(t1, t2)
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

    merged = merge_bst(t1, t2)
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

    merged = merge_bst(t2, t1)
    merged.show()


def example4():
    t1 = BinarySearchTree()
    t1.insert(2)
    t1.insert(1)
    t1.insert(3)

    t2 = BinarySearchTree()
    t2.insert(4)

    merged = merge_bst(t1, t2)
    merged.show()


example4()
