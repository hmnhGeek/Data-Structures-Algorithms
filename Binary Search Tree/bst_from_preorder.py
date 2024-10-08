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
        self.d = 1

    def recalc_aug(self, parent: Node):
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

    def get_leftmost_leaf(self, node: Node):
        if node is None:
            return

        while node.left is not None:
            node = node.left

        return node

    def get_rightmost_leaf(self, node: Node):
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

    def get_node(self, start: Node, data):
        if start is None or data is None:
            return

        if start.data == data:
            return start

        if data >= start.data:
            return self.get_node(start.right, data)

        return self.get_node(start.left, data)

    def delete(self, x):
        node = self.get_node(self.root, x)
        return self._delete(node)

    def _show(self, start: Node):
        if start:
            self._show(start.left)
            print(
                f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)


def construct_tree_from_preorder(preorder) -> BinarySearchTree:
    # Overall time complexity is O(N * log(N)) and space is O(1).

    # Create a blank BST
    binary_search_tree = BinarySearchTree()

    # The first data point in the preorder list is always root node.
    # insert the root node in O(1) time.
    root_data = preorder[0]
    binary_search_tree.insert(root_data)

    # insert all the nodes from 1st index from the preorder list.
    # this will take O(N * log(N)) time
    for index in range(1, len(preorder)):
        binary_search_tree.insert(preorder[index])
    return binary_search_tree


# Example
preorder = [10, 5, 1, 7, 40, 50]
tree = construct_tree_from_preorder(preorder)
tree.show()
print()
preorder2 = [22, 12, 8, 20, 30, 25, 40]
tree2 = construct_tree_from_preorder(preorder2)
tree2.show()
print()
preorder3 = [100, 20, 10, 30, 200, 150, 300]
tree3 = construct_tree_from_preorder(preorder3)
tree3.show()