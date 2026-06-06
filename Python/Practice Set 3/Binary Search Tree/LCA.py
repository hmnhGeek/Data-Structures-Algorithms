# Problem link - https://www.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1


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

    def _insert(self, root, node):
        if root is None or node is None:
            return
        if node.data >= root.data:
            if root.right is not None:
                self._insert(root.right, node)
                return
            root.right = node
            node.parent = root
            self.recalc_augmentation(root)
            return
        if root.left is not None:
            self._insert(root.left, node)
            return
        root.left = node
        node.parent = root
        self.recalc_augmentation(root)
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
        node = self._get_node(self.root, x)
        self._delete(node)

    def _get_node(self, start, x):
        if start is None or x is None:
            return
        if start.data == x:
            return start
        if x >= start.data:
            return self._get_node(start.right, x)
        return self._get_node(start.left, x)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root),' if start == self.root else ','} size = {start.size}, height = {start.height}, d = {start.diameter}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def _get_common_starting_pt(node1, depth1, node2, depth2):
        diff = abs(depth2 - depth1)
        if depth1 < depth2:
            for _ in range(diff):
                node2 = node2.parent
        elif depth1 > depth2:
            for _ in range(diff):
                node1 = node1.parent
        return node1, node2

    @staticmethod
    def _get_depth(bst, node):
        depth = 0
        while node != bst.root:
            node = node.parent
            depth += 1
        return depth

    @staticmethod
    def get_lca(bst: BinarySearchTree, n1, n2):
        """
            Time complexity is O(log(n)) and space complexity is O(log(n)).
        """

        # finding nodes take O(log(n)) time and O(log(n)) space.
        node1 = bst._get_node(bst.root, n1)
        node2 = bst._get_node(bst.root, n2)
        if node1 is None or node2 is None:
            return

        # finding depth takes O(log(n)) time
        depth1 = Solution._get_depth(bst, node1)
        depth2 = Solution._get_depth(bst, node2)

        # This process also takes O(log(n)) time.
        node1, node2 = Solution._get_common_starting_pt(node1, depth1, node2, depth2)

        # This process takes O(log(n)) time.
        while node1 != node2:
            node1 = node1.parent
            node2 = node2.parent
        return node1.data


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
