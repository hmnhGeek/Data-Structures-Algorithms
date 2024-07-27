class Node:
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data
        self.next = None
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
            left_ht, right_ht = parent.left.ht if parent.left else 0, parent.right.ht if parent.right else 0

            parent.size = 1 + left_sz + right_sz
            parent.ht = 1 + max(left_ht, right_ht)
            parent.d = 1 + left_ht + right_ht
            parent.next = self.get_successor(parent)
            self.d = max(self.d, parent.d)
            parent = parent.parent

    def _insert(self, start, node):
        if start is None or node is None:
            return
        if node.data >= start.data:
            if start.right is not None:
                return self._insert(start.right, node)
            else:
                start.right = node
                node.parent = start
                node.next = self.get_successor(node)
                self.recalc_aug(start)
                return

        if start.left is not None:
            return self._insert(start.left, node)
        start.left = node
        node.parent = start
        node.next = self.get_successor(node)
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

            del node
            self.recalc_aug(parent)
            return

        if node.right is not None:
            s = self.get_successor(node)
            s.data, node.data = node.data, s.data
            return self._delete(s)

        p = self.get_predecessor(node)
        p.data, node.data = node.data, p.data
        return self._delete(p)

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
                return None

        return parent

    def get_leftmost_leaf(self, node):
        if node is None:
            return

        while node.left is not None:
            node = node.left

        return node

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

    def get_rightmost_leaf(self, node):
        if node is None:
            return

        while node.right is not None:
            node = node.right

        return node

    def delete(self, x):
        node = self.get_node(self.root, x)
        if node is not None:
            return self._delete(node)

    def get_node(self, start, x):
        if x is None or start is None:
            return

        if x == start.data:
            return start
        if x >= start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, next = {start.next.data if start.next else None}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)


def find_lowest_common_ancestor(tree: BinarySearchTree, x, y) -> Node:
    '''
        Overall time complexity is O(log(n)) and overall space complexity is O(log(n))
        where n is the number of nodes in the tree.

        This solution was made easy because there is a parent pointer for each node. In case
        parent pointers were not used, we would have started traversing from root downwards and
        stored nodes in a set for finding node x. Then again start from root to find y. At any point
        when the node in the path and the node in the set is different, return the previously
        stored same node as lowest common ancestor.
    '''

    if x is None or y is None:
        return

    # takes O(log(n)) time and O(log(n)) space for recursion stack
    nodex = tree.get_node(tree.root, x)

    # takes O(log(n)) time and O(log(n)) space for recursion stack
    nodey = tree.get_node(tree.root, y)

    # will hold O(log(n)) space till the root.
    x_ancestors = set()

    # this will take O(log(n)) time to reach root node.
    curr = nodex
    while curr is not None:
        x_ancestors.add(curr)
        curr = curr.parent

    # this will take O(log(n)) time to reach root node.
    curr = nodey
    while curr is not None:
        # will take O(1) amortized time for set.
        if curr in x_ancestors:
            return curr
        curr = curr.parent

    return None


def example1():
    t = BinarySearchTree()
    l = [2, 6, 8, 0, 9, 9, 7]
    for i in l:
        t.insert(i)

    print("\n\nFor tree with following inorder: \n")
    t.show()

    print(
        find_lowest_common_ancestor(t, 9, 7).data
    )

    print(
        find_lowest_common_ancestor(t, 9, 8).data
    )

    print(
        find_lowest_common_ancestor(t, 0, 8).data
    )

def example2():
    tree = BinarySearchTree()

    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(3)
    tree.insert(7)
    tree.insert(8)

    print("\n\nFor tree with following inorder: \n")
    tree.show()

    print(
        find_lowest_common_ancestor(tree, 7, 8).data
    )

    print(
        find_lowest_common_ancestor(tree, 3, 6).data
    )


def example3():
    tree = BinarySearchTree()

    tree.insert(2)
    tree.insert(1)
    tree.insert(3)

    print("\n\nFor tree with following inorder: \n")
    tree.show()

    print(
        find_lowest_common_ancestor(tree, 1, 3).data
    )

example1()
example2()
example3()