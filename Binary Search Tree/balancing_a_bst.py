# Problem link - https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/


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
            left_size = parent.left.size if parent.left else 0
            right_size = parent.right.size if parent.right else 0

            left_ht = parent.left.ht if parent.left else 0
            right_ht = parent.right.ht if parent.right else 0

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
        if x is None:
            return

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
        if x is None or start is None:
            return

        if start.data == x:
            return start
        if x >= start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def delete(self, x):
        node = self.get_node(self.root, x)
        if node is not None:
            return self._delete(node)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Node = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, ht = {start.ht}, d = {start.d}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class BSTBalancer:
    def __init__(self, bst: BinarySearchTree):
        self.bst = bst

    def get_inorder(self, start, inorder_traversal):
        if start:
            self.get_inorder(start.left, inorder_traversal)
            inorder_traversal.append(start.data)
            self.get_inorder(start.right, inorder_traversal)

    def balanced_insert(self, balanced_bst, low, high, inorder):
        if low > high:
            return

        # find the mid-element from inorder traversal and insert it into the balanced BST
        mid = (low + high) // 2
        balanced_bst.insert(inorder[mid])

        # use left split to insert into left subtree
        self.balanced_insert(balanced_bst, low, mid - 1, inorder)

        # user right split to insert into right subtree
        self.balanced_insert(balanced_bst, mid + 1, high, inorder)

    def balance(self):
        # Overall time complexity is O(N) and space complexity is O(N + log(N)) with log(N) coming from recursion
        # stack space.

        # first fetch the inorder traversal of the unbalanced BST in O(N) time and O(N) space.
        inorder_traversal = []
        self.get_inorder(self.bst.root, inorder_traversal)

        # create a new BST which would be balanced.
        balanced_bst = BinarySearchTree()

        # the idea is to insert into the balanced BST using the inorder traversal by repetitively splitting the list
        # into half and inserting the `mid` element. The left half split will be used recursively to insert into left
        # subtree and the right half split will be used recursively to insert into the right subtree. This would take
        # O(N) time as we are traversing for each node in the inorder traversal, however, the stack space would be
        # only O(log(N)).
        n = len(inorder_traversal)
        low, high = 0, n - 1
        self.balanced_insert(balanced_bst, low, high, inorder_traversal)

        # once the balanced BST is populated, delete the unbalanced tree and refer to the updated balanced BST.
        unbalanced_bst = self.bst
        self.bst = balanced_bst
        del unbalanced_bst


def example1():
    bst = BinarySearchTree()
    bst.insert(30)
    bst.insert(20)
    bst.insert(10)
    bst.show()
    BSTBalancer(bst).balance()
    bst.show()


def example2():
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.show()
    BSTBalancer(bst).balance()
    bst.show()


def example3():
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(3)
    bst.insert(2)
    bst.insert(1)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.show()
    BSTBalancer(bst).balance()
    bst.show()


print("Example 1")
example1()
print("\nExample 2")
example2()
print("\nExample 3")
example3()
