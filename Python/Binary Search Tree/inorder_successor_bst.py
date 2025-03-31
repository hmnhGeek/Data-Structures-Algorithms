class Node:
    def __init__(self, data):
        self.parent, self.left, self.data, self.right, self.next, self.size, self.ht, self.d = None, None, data, None, None, 1, 1, 1


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
            # for each parent, ensure that we update its successor.
            parent.next = self.get_successor(parent)
            self.d = max(self.d, parent.d)

            parent = parent.parent

    def _insert(self, start, node):
        if start is None or node is None: return
        if node.data >= start.data:
            if start.right is not None: return self._insert(start.right, node)
            else:
                start.right = node
                node.parent = start

                # because we are starting recalculation of augmentation from parent, manually assign next pointer for
                # the inserting node.
                node.next = self.get_successor(node)
                self.recalc_aug(start)
                return

        if start.left is not None: return self._insert(start.left, node)
        else:
            start.left = node
            node.parent = start

            # because we are starting recalculation of augmentation from parent, manually assign next pointer for the
            # inserting node.
            node.next = self.get_successor(node)
            self.recalc_aug(start)
            return

    def insert(self, x):
        if x is None: return
        node = Node(x)

        if self.root is None:
            self.root = node
            self.d = 1
            return

        return self._insert(self.root, node)

    def get_leftmost_leaf(self, node):
        if node is None: return

        while node.left is not None:
            node = node.left

        return node

    def get_rightmost_leaf(self, node):
        if node is None: return

        while node.right is not None:
            node = node.right

        return node

    def get_successor(self, node):
        if node is None: return
        if node.right is not None: return self.get_leftmost_leaf(node.right)

        parent = node.parent
        if parent is None: return
        while parent.left != node:
            node = node.parent
            parent = parent.parent
            if parent is None: return

        return parent

    def get_predecessor(self, node):
        if node is None: return
        if node.left is not None: return self.get_rightmost_leaf(node.left)

        parent = node.parent
        if parent is None: return
        while parent.right != node:
            node = node.parent
            parent = parent.parent
            if parent is None: return

        return parent

    def _delete(self, node):
        if node is None: return
        if node.left is None and node.right is None:
            parent = node.parent

            if parent is not None:
                if parent.left == node: parent.left = None
                else: parent.right = None
            else:
                self.root = None
                self.d = 0

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

    def get_node(self, start, x):
        if start is None or x is None: return
        if start.data == x: return start
        if x >= start.data: return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def delete(self, x):
        if x is None: return
        node = self.get_node(self.root, x)
        if node is not None:
            return self._delete(node)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}, next = {start.next.data if start.next else None}")
            self._show(start.right)

    def show(self):
        print()
        self._show(self.root)


def example1():
    t = BinarySearchTree()
    l = [2, 6, 8, 0, 9, 9, 7]

    for i in l:
        t.insert(i)

    t.show()
    t.delete(8)
    t.show()
    t.delete(2)
    t.show()
    t.delete(0)
    t.show()
    t.delete(7)
    t.show()
    t.delete(9)
    t.show()
    t.delete(6)
    t.show()
    t.delete(9)
    t.show()

def example2():
    t = BinarySearchTree()
    l = [8, 7, 9, 7, 8, 8, 8, 0, 3, 6]
    for i in l:
        t.insert(i)

    t.show()
    t.delete(8)
    t.show()
    t.delete(8)
    t.show()
    t.delete(8)
    t.show()
    t.delete(7)
    t.show()


print("This is example 1: List = [2, 6, 8, 0, 9, 9, 7]")
example1()

print("This is example 2: List = [8, 7, 9, 7, 8, 8, 8, 0, 3, 6]")
example2()
