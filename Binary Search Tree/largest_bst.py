class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.data = data
        self.right = None
        self.size = 1
        self.ht = 1
        self.d = 1


class BTNode:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


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

    def _insert(self, start: Node, node: Node):
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

    def get_successor(self, node: Node):
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

    def get_predecessor(self, node: Node):
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

    def _delete(self, node: Node):
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
        if data > start.data:
            return self.get_node(start.right, data)
        return self.get_node(start.left, data)

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


class Vector:
    def __init__(self, size, max_val, min_val):
        self.size = size
        self.max_val = max_val
        self.min_val = min_val


class MaxSizeBSTFinder:
    @staticmethod
    def find_max_size(root: Node):
        # if the root node is None, return a vector <size: 0, max: -inf, min: inf>
        if root is None:
            return Vector(0, -1e6, 1e6)

        left_result = MaxSizeBSTFinder.find_max_size(root.left)
        right_result = MaxSizeBSTFinder.find_max_size(root.right)
        if left_result.max_val < root.data < right_result.min_val:
            return Vector(
                1 + left_result.size + right_result.size,
                max(left_result.max_val, root.data, right_result.max_val),
                min(left_result.min_val, root.data, right_result.min_val)
            )
        else:
            return Vector(
                max(left_result.size, right_result.size),
                1e6,
                -1e6
            )

# Example 1
n20, n15, n40, n14, n18, n30, n60, n17, n16, n19, n50 = BTNode(20), BTNode(15), BTNode(40), BTNode(14), BTNode(18), BTNode(30), BTNode(60), BTNode(17), BTNode(16), BTNode(19), BTNode(50)
n20.left = n15
n15.left = n14
n18.left = n16
n40.left = n30
n60.left = n50
n20.right = n40
n40.right = n60
n15.right = n18
n18.right = n19
n14.right = n17
print(MaxSizeBSTFinder.find_max_size(n20).size)


# Example 2
n10 = BTNode(10)
n5 = BTNode(5)
n15 = BTNode(15)
n1 = BTNode(1)
n8 = BTNode(8)
n7 = BTNode(7)
n10.left = n5
n5.left = n1
n5.right = n8
n10.right = n15
n15.right = n7
print(MaxSizeBSTFinder.find_max_size(n10).size)