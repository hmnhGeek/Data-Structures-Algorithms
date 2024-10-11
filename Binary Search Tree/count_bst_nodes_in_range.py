# Problem link - https://www.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1


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
            left_size, right_size = parent.left.size if parent.left else 0, parent.right.size if parent.right else 0
            left_ht, right_ht = parent.left.ht if parent.left else 0, parent.right.ht if parent.right else 0
            parent.size = 1 + left_size + right_size
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

    def get_node(self, start, x):
        if start is None or x is None:
            return
        if start.data == x:
            return start
        if x >= start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def delete(self, x):
        node = self.get_node(self.root, x)
        if node:
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
    def _populate_nodes(root: Node, low: int, high: int, result: list):
        # if the node is None, return from the recursion stack.
        if root is None:
            return

        # if the current node's data is in inclusive range, then...
        if low <= root.data <= high:
            # push the data into the result list
            result.append(root.data)
            # search in left subtree with high <-- data - 1 (because now we don't want inclusive high).
            Solution._populate_nodes(root.left, low, root.data - 1, result)
            # search in the right subtree with low <-- data
            Solution._populate_nodes(root.right, root.data, high, result)

        # if the root's data is not in the range, there are two possibilities...
        # the node's data < low
        elif root.data < low:
            # it means there is no point in searching in left subtree, so search in right with same range.
            Solution._populate_nodes(root.right, low, high, result)
        else:
            # else if data > high, it means there is no point in searching in right subtree, so search in left with the
            # same range.
            Solution._populate_nodes(root.left, low, high, result)

    @staticmethod
    def get_nodes_in_range(bst: BinarySearchTree, low: int, high: int):
        """
            Overall time complexity is O(n) and space complexity is also O(n).
        """

        # create a blank list to store the results
        result = []
        # if the range is invalid, return blank list.
        if low > high:
            return result
        # populate the result list in O(n) time and O(n) recursion stack space.
        Solution._populate_nodes(bst.root, low, high, result)
        # return the result.
        return result


# Example 1
tree1 = BinarySearchTree()
tree1.insert(10)
tree1.insert(5)
tree1.insert(50)
tree1.insert(1)
tree1.insert(40)
tree1.insert(100)
print(Solution.get_nodes_in_range(tree1, 5, 45))

# Example 2
tree2 = BinarySearchTree()
for i in [5, 4, 6, 3, 7]:
    tree2.insert(i)
print(Solution.get_nodes_in_range(tree2, 2, 8))

# Example 3
tree3 = BinarySearchTree()
for i in [10, 5, 15, 3, 7, 18]:
    tree3.insert(i)
print(Solution.get_nodes_in_range(tree3, 7, 15))

# Example 4
tree4 = BinarySearchTree()
for i in [10, 5, 15, 3, 7, 13, 18, 1, 6]:
    tree4.insert(i)
print(Solution.get_nodes_in_range(tree4, 6, 10))