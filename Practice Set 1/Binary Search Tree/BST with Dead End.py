# Problem link - https://www.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.size = self.d = self.ht = 1


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
            parent = parent.parent

    def _insert(self, start, node):
        if node is None or start is None:
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
    def _get_inorder(root: Node, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root)
            Solution._get_inorder(root.right, inorder)

    @staticmethod
    def contains_dead_ends(bst: BinarySearchTree):
        """
            Overall time complexity is O(n) and space complexity is O(n).
        """

        # get the inorder of the tree in O(n) time and O(n) space.
        inorder = []
        Solution._get_inorder(bst.root, inorder)

        # if there is only 1 node or no nodes at all in the BST, then there is no dead end inside it.
        n = len(inorder)
        if n == 0 or n == 1:
            return False

        # however, specifically check for the first node
        first_node = inorder[0]

        # since there can be no duplicate nodes, first node can be a dead end only if it is 1 and the next node is 2.
        if first_node.left is None and first_node.right is None and first_node.data == 1 and inorder[1].data == 2:
            return True

        # now loop on all the nodes in this inclusive range [1, n - 2].
        for i in range(1, n - 1):
            # get prev, current and next nodes
            prev, node, next_node = inorder[i - 1], inorder[i], inorder[i + 1]

            # if current node is a leaf node and,
            if node.left is None and node.right is None:
                # prev + 1 = node and node + 1 = next, then current node is a dead end, return True
                if prev.data + 1 == node.data == next_node.data - 1:
                    return True

        # last node can never be a dead end, return False finally.
        return False


# Example 1
bst = BinarySearchTree()
for i in [8, 5, 9, 2, 7, 1]:
    bst.insert(i)
print(Solution.contains_dead_ends(bst))

# Example 2
bst = BinarySearchTree()
for i in [8, 7, 10, 2, 9, 13]:
    bst.insert(i)
print(Solution.contains_dead_ends(bst))

# Example 3
bst = BinarySearchTree()
for i in [10, 6, 12, 2, 8, 11, 15]:
    bst.insert(i)
print(Solution.contains_dead_ends(bst))

# Example 4
bst = BinarySearchTree()
for i in [7, 4, 8]:
    bst.insert(i)
print(Solution.contains_dead_ends(bst))
