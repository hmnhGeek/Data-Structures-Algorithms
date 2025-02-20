# Problem link - https://www.geeksforgeeks.org/problems/brothers-from-different-root/1


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
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
    def _inorder(root, inorder):
        if root:
            Solution._inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._inorder(root.right, inorder)

    @staticmethod
    def _get_inorder(bst: BinarySearchTree):
        inorder = []
        Solution._inorder(bst.root, inorder)
        return inorder

    @staticmethod
    def find(bst1: BinarySearchTree, bst2: BinarySearchTree, x: int):
        """
            Overall time complexity is O(n * log(m)) and space complexity is O(log(n) + log(m))
        """

        # get inorder of bst1 in O(n) time and O(log(n)) space.
        inorder1 = Solution._get_inorder(bst1)
        # store the pairs in result array
        result = []
        # loop on the data points from bst1's inorder.
        for data in inorder1:
            # check if x - data node is present in bst2 in O(log(m)) time and O(log(m)) space.
            node = bst2.get_node(bst2.root, x - data)
            if node is not None:
                result.append((data, node.data))
        # return the result
        return result

    @staticmethod
    def find_v2(bst1: BinarySearchTree, bst2: BinarySearchTree, x: int):
        """
            Overall time complexity is O(n + m) and space complexity is O(n + m).
        """

        # get inorder of bst1 in O(n) time and O(log(n)) space.
        inorder1 = Solution._get_inorder(bst1)
        # get inorder of bst2 in O(m) time and O(log(m)) space.
        inorder2 = Solution._get_inorder(bst2)

        # store the pairs in result array
        result = []

        # take two pointers and place them at extremes, `i` will be on inorder1.
        i, j = 0, len(inorder2) - 1

        # while both indices are within bounds
        while 0 <= i < len(inorder1) and 0 <= j < len(inorder2):
            _sum = inorder1[i] + inorder2[j]
            if _sum == x:
                result.append((inorder1[i], inorder2[j]))
                i += 1
                j -= 1
            elif _sum > x:
                j -= 1
            else:
                i += 1
        # return the result
        return result


# Example 1
bst1 = BinarySearchTree()
for i in [5, 3, 7, 2, 4, 6, 8]:
    bst1.insert(i)
bst2 = BinarySearchTree()
for i in [10, 6, 15, 3, 8, 11, 18]:
    bst2.insert(i)
print(Solution.find(bst1, bst2, 16))
print(Solution.find_v2(bst1, bst2, 16))


# Example 2
bst1 = BinarySearchTree()
for i in [1, 3, 2]:
    bst1.insert(i)
bst2 = BinarySearchTree()
for i in [3, 2, 4, 1]:
    bst2.insert(i)
print(Solution.find(bst1, bst2, 4))
print(Solution.find_v2(bst1, bst2, 4))
