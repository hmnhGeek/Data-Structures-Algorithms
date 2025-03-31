# Problem link - https://www.geeksforgeeks.org/problems/merge-two-bst-s/1


from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.d = self.size = self.ht = 1


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
            self.recalc_aug(parent)
            del node
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
        if data == start.data:
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


class Solution:
    @staticmethod
    def _get_inorder(root: Node, inorder: List[int]):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def _get_inorder_data(bst: BinarySearchTree) -> List[int]:
        inorder = []
        Solution._get_inorder(bst.root, inorder)
        return inorder

    @staticmethod
    def _merge(x: List[int], y: List[int]) -> List[int]:
        merged = []
        i, j = 0, 0
        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                merged.append(x[i])
                i += 1
            else:
                merged.append(y[j])
                j += 1
        while i < len(x):
            merged.append(x[i])
            i += 1
        while j < len(y):
            merged.append(y[j])
            j += 1
        return merged

    @staticmethod
    def _build_merged_bst(inorder: List[int], bst: BinarySearchTree, low: int, high: int):
        if low > high:
            return
        mid = int(low + (high - low)/2)
        bst.insert(inorder[mid])
        Solution._build_merged_bst(inorder, bst, low, mid - 1)
        Solution._build_merged_bst(inorder, bst, mid + 1, high)

    @staticmethod
    def merge_bsts(bst1: BinarySearchTree, bst2: BinarySearchTree) -> BinarySearchTree:
        """
            Overall time complexity is O(m + n) and space complexity is O(log(n) + log(m) + n + m + log(n + m))
            or O(n + m) space.
        """

        # get inorders in O(n + m) time and O(h1 + h2) space.
        inorder1 = Solution._get_inorder_data(bst1)
        inorder2 = Solution._get_inorder_data(bst2)
        # merge the inorder lists in O(n + m) time and O(n + m) space.
        merged_inorder = Solution._merge(inorder1, inorder2)
        # get the merged BST in O(m + n) time and O(log(m + n)) space.
        merged_bst = BinarySearchTree()
        Solution._build_merged_bst(merged_inorder, merged_bst, 0, len(merged_inorder) - 1)
        return merged_bst


# Example 1
bst1 = BinarySearchTree()
for i in [5, 3, 6, 2, 4]:
    bst1.insert(i)
bst2 = BinarySearchTree()
for i in [2, 1, 3, 7, 6]:
    bst2.insert(i)
bst1.show()
bst2.show()
merged_bst = Solution.merge_bsts(bst1, bst2)
merged_bst.show()


# Example 2
bst1 = BinarySearchTree()
for i in [12, 9, 6, 11]:
    bst1.insert(i)
bst2 = BinarySearchTree()
for i in [8, 5, 10, 2]:
    bst2.insert(i)
bst1.show()
bst2.show()
merged_bst = Solution.merge_bsts(bst1, bst2)
merged_bst.show()