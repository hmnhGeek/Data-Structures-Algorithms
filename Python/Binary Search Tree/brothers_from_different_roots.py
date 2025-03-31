# Problem link - https://www.geeksforgeeks.org/problems/brothers-from-different-root/1
# Solution - https://www.youtube.com/watch?v=jZlQLrK14Bw&t=335s


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
        if data >= start.data:
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


class BstWithTraversal(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def _get_inorder(self, root, inorder):
        if root is not None:
            self._get_inorder(root.left, inorder)
            inorder.append(root.data)
            self._get_inorder(root.right, inorder)

    def get_inorder(self):
        inorder = []
        self._get_inorder(self.root, inorder)
        return inorder


class SiblingsFinder:
    def __init__(self, bst1: BstWithTraversal, bst2: BstWithTraversal):
        self.bst1 = bst1
        self.bst2 = bst2

    def find_pairs_with_sum(self, k: int):
        # Time complexity is O(n) for traversing the trees (i.e., n1 + n2). Space complexity is
        # O(n1 + n2) = O(n) for storing the inorder traversals.

        # store a result list for storing the pairs from both trees whose sum is k.
        result = []

        # get the inorder traversal of both trees. Note that these will be sorted arrays.
        inorder1 = self.bst1.get_inorder()
        inorder2 = self.bst2.get_inorder()

        # create two pointers in which `i` starts from 0th index of first tree
        # and `j` starts from the last index of the second tree.
        i, j = 0, len(inorder2) - 1

        # while both i and j are in bounds.
        while i < len(inorder1) and j >= 0:
            # get the current sum
            curr_sum = inorder1[i] + inorder2[j]

            # if the current sum is same as k, add it to result and decrement `j`.
            # no need to increment `i`.
            if curr_sum == k:
                result.append((inorder1[i], inorder2[j]))
                j -= 1
            elif curr_sum < k:
                # else if current sum is less than k, then we must increase the sum by incrementing `i`.
                i += 1
            else:
                # else if sum is higher than `k`, decrease the sum by decrementing `j`.
                j -= 1

        # finally return the result.
        return result


# Example 1
t1 = BstWithTraversal()
t2 = BstWithTraversal()
t1.insert(5)
t1.insert(3)
t1.insert(7)
t1.insert(2)
t1.insert(4)
t1.insert(6)
t1.insert(8)
t2.insert(10)
t2.insert(6)
t2.insert(15)
t2.insert(3)
t2.insert(8)
t2.insert(11)
t2.insert(18)
print(SiblingsFinder(t1, t2).find_pairs_with_sum(16))


# Example 2
t1 = BstWithTraversal()
t2 = BstWithTraversal()
t1.insert(1)
t1.insert(3)
t1.insert(2)
t2.insert(3)
t2.insert(2)
t2.insert(4)
t2.insert(1)
print(SiblingsFinder(t1, t2).find_pairs_with_sum(4))