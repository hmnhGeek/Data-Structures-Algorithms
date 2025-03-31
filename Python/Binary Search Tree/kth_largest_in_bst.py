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
            left_sz, right_sz = parent.left.size if parent.left else 0, parent.right.size if parent.right else 0
            left_ht, right_ht = parent.right.ht if parent.right else 0, parent.right.ht if parent.right else 0

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
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)

    def _get_inorder(self, start, inorder):
        if start:
            self._get_inorder(start.left, inorder)
            inorder.append(start)
            self._get_inorder(start.right, inorder)

    def get_inorder(self):
        inorder = []
        self._get_inorder(self.root, inorder)
        return inorder

    def get_kth_largest(self, k):
        # This method will take O(N) time and O(N) space.
        inorder = self.get_inorder()
        if k > len(inorder) or k <= 0:
            return
        return inorder[len(inorder) - k].data

    def get_kth_smallest(self, k):
        # This method will take O(N) time and O(N) space.
        inorder = self.get_inorder()
        if k > len(inorder) or k <= 0:
            return
        return inorder[k - 1].data


# Example 1
tree1 = BinarySearchTree()
tree1.insert(4)
tree1.insert(2)
tree1.insert(9)
tree1.show()
print(tree1.get_kth_largest(2))

# Example 2
tree2 = BinarySearchTree()
tree2.insert(9)
tree2.insert(10)
tree2.show()
print(tree2.get_kth_largest(1))

# Example 3
tree3 = BinarySearchTree()
tree3.insert(2)
tree3.insert(1)
tree3.insert(3)
tree3.show()
print(tree3.get_kth_smallest(2))
print(tree3.get_kth_smallest(5))