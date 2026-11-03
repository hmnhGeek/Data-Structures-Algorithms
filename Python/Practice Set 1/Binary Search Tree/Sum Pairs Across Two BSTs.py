# Problem link - https://www.geeksforgeeks.org/problems/brothers-from-different-root/1


class Node:
    def __init__(self, data):
        self.data = data
        self.height = self.size = self.diameter = 1
        self.left = self.right = self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.diameter = 0

    def recalculate_augmentation(self, parent):
        self.diameter = 0
        while parent is not None:
            left_size = parent.left.size if parent.left is not None else 0
            left_height = parent.left.height if parent.left is not None else 0
            right_size = parent.right.size if parent.right is not None else 0
            right_height = parent.right.height if parent.right is not None else 0
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

    def _insert(self, start, node):
        if start is None or node is None:
            return
        if node.data >= start.data:
            if start.right is not None:
                self._insert(start.right, node)
                return
            start.right = node
            node.parent = start
            self.recalculate_augmentation(start)
            return
        if start.left is not None:
            self._insert(start.left, node)
            return
        start.left = node
        node.parent = start
        self.recalculate_augmentation(start)
        return

    def get_leftmost_node(self, node):
        if node is None:
            return
        while node.left is not None:
            node = node.left
        return node

    def get_rightmost_node(self, node):
        if node is None:
            return
        while node.right is not None:
            node = node.right
        return node

    def get_successor(self, node):
        if node is None:
            return
        if node.right is not None:
            return self.get_leftmost_node(node.right)
        parent = node.parent
        if parent is None:
            return
        while parent.left != node:
            node = node.parent
            parent = parent.parent
            if parent is None:
                return None
        return parent

    def get_predecessor(self, node):
        if node is None:
            return
        if node.left is not None:
            return self.get_rightmost_node(node.left)
        parent = node.parent
        if parent is None:
            return
        while parent.right != node:
            node = node.parent
            parent = parent.parent
            if parent is None:
                return None
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
                self.diameter = 0
                self.root = None
            del node
            self.recalculate_augmentation(parent)
            return
        if node.right is not None:
            successor = self.get_successor(node)
            successor.data, node.data = node.data, successor.data
            return self._delete(successor)
        predecessor = self.get_predecessor(node)
        predecessor.data, node.data = node.data, predecessor.data
        return self._delete(predecessor)

    def delete(self, x):
        node = self.get_node(self.root, x)
        return self._delete(node)

    def get_node(self, start, x):
        if start is None or x is None:
            return
        if start.data == x:
            return start
        if x > start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}, size = {start.size}, height = {start.height}, diameter = {start.diameter}")
            self._show(start.right)

    def show(self):
        self._show(self.root)
        print()


class Solution:
    @staticmethod
    def get_pairs(bst1: BinarySearchTree, bst2: BinarySearchTree, x: int) -> int:
        """
            Time complexity is O(n + m) and space complexity is O(n + m).
        """
        pairs_count = 0

        # these will take O(n + m) space
        inorder1, inorder2 = [], []

        # These both take O(n + m) time and O(log(n) + log(m)) time.
        Solution._get_inorder(bst1.root, inorder1)
        Solution._get_inorder(bst2.root, inorder2)

        # This will run for O(n + m) time
        i = len(inorder1) - 1
        j = 0
        while i >= 0 and j < len(inorder2):
            _sum = inorder1[i] + inorder2[j]
            if _sum == x:
                pairs_count += 1
                i -= 1
                j += 1
            elif _sum < x:
                j += 1
            else:
                i -= 1
        return pairs_count

    @staticmethod
    def _get_inorder(root, inorder):
        if root:
            Solution._get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution._get_inorder(root.right, inorder)


def test(arr1, arr2, x):
    bst1 = BinarySearchTree()
    for i in arr1:
        bst1.insert(i)
    bst2 = BinarySearchTree()
    for i in arr2:
        bst2.insert(i)
    print(Solution.get_pairs(bst1, bst2, x))


if __name__ == "__main__":
    test([2, 1, 3], [5, 4, 6], 6)
    test([7, 5, 10, 1], [2, 6], 9)
    test([5, 3, 7, 2, 4, 6, 8], [10, 6, 15, 3, 8, 11, 18], 16)
    test([1, 3, 2], [3, 2, 4, 1], 4)
