# Problem link - https://www.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1


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
    def _find_count_of_nodes_in_range(root: Node, low, high, counter, nodes):
        # if the node is None, return from the recursion stack, as we've reached to the bottom of the BST.
        if root is None:
            return

        # if the root's data is even higher than the `high`, there's no point in searching in the right subtree. Search
        # only in left subtree.
        if root.data > high:
            Solution._find_count_of_nodes_in_range(root.left, low, high, counter, nodes)

        # if the root's data is even lower than the `low`, there's no point in searching in the left subtree. Search
        # only in right subtree.
        elif root.data < low:
            Solution._find_count_of_nodes_in_range(root.right, low, high, counter, nodes)

        # if however, root is in [low, high]...
        elif low <= root.data <= high:
            # increment the count of nodes found and add the root into the nodes list.
            counter[0] += 1
            nodes.append(root.data)

            # now search in the left and right subtrees with shrunk ranges.
            Solution._find_count_of_nodes_in_range(root.left, low, root.data, counter, nodes)
            Solution._find_count_of_nodes_in_range(root.right, root.data, high, counter, nodes)

    @staticmethod
    def count_nodes(bst: BinarySearchTree, low, high):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        counter = [0]
        nodes = []
        Solution._find_count_of_nodes_in_range(bst.root, low, high, counter, nodes)
        # return the count of nodes and the actual nodes.
        return counter[0], nodes


# Example 1
tree1 = BinarySearchTree()
tree1.insert(10)
tree1.insert(5)
tree1.insert(50)
tree1.insert(1)
tree1.insert(40)
tree1.insert(100)
print(Solution.count_nodes(tree1, 5, 45))

# Example 2
tree2 = BinarySearchTree()
for i in [5, 4, 6, 3, 7]:
    tree2.insert(i)
print(Solution.count_nodes(tree2, 2, 8))

# Example 3
tree3 = BinarySearchTree()
for i in [10, 5, 15, 3, 7, 18]:
    tree3.insert(i)
print(Solution.count_nodes(tree3, 7, 15))

# Example 4
tree4 = BinarySearchTree()
for i in [10, 5, 15, 3, 7, 13, 18, 1, 6]:
    tree4.insert(i)
print(Solution.count_nodes(tree4, 6, 10))
