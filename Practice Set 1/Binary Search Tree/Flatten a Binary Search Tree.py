# Problem link - https://www.geeksforgeeks.org/flatten-bst-to-sorted-list-increasing-order/
# Solution - https://www.youtube.com/watch?v=NzXtnzQTouk


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
    def _flatten(root: Node):
        # if root node is Null, return from recursion.
        if root is None:
            return

        # get the head of the flattened list from the left subtree
        head = Solution._flatten(root.left)

        # break the root's left link
        root.left = None

        # if left subtree was not present, head would be none, in that case make root as head.
        if head is None:
            head = root
        else:
            # else traverse to the last node of the flattened list
            temp = head
            while temp is not None and temp.right is not None:
                temp = temp.right
            # make temp's right as root
            temp.right = root

        # also, root's right will point to the head of the flattened list from right subtree
        root.right = Solution._flatten(root.right)

        # return the head of the left subtree which would be the head of the entire flattened tree.
        return head

    @staticmethod
    def flatten(bst: BinarySearchTree):
        """
            Overall time complexity is O(n) and space complexity is O(h).
        """

        # get the root of the flattened tree in O(n) time and O(h) space.
        flattened_root = Solution._flatten(bst.root)
        while flattened_root is not None:
            print(flattened_root.data, end=" ")
            flattened_root = flattened_root.right
        print()


t = BinarySearchTree()
for i in [5, 3, 7, 2, 4, 6, 8]:
    t.insert(i)
t.show()
Solution.flatten(t)

t2 = BinarySearchTree()
for i in [8,9,2,6,4,8,9,1]:
    t2.insert(i)
t2.show()
Solution.flatten(t2)
