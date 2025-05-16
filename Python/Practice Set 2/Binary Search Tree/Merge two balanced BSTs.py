# Problem link - https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None
        self.ht = self.size = self.d = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.d = 0

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

    def delete(self, x):
        node = self.get_node(self.root, x)
        if node is not None:
            return self._delete(node)

    def get_node(self, start, x):
        if start is None or x is None:
            return
        if x == start.data:
            return start
        if x > start.data:
            return self.get_node(start.right, x)
        return self.get_node(start.left, x)

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
    def get_inorder(root, inorder):
        # Perform inorder traversal and collect node values in the 'inorder' list
        if root:
            Solution.get_inorder(root.left, inorder)
            inorder.append(root.data)
            Solution.get_inorder(root.right, inorder)

    @staticmethod
    def _get_merged_inorder(left, right):
        # Merge two sorted inorder traversal lists into one sorted list
        merged = []
        i, j = 0, 0

        # Merge elements from both lists in sorted order
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append any remaining elements from the left list
        while i < len(left):
            merged.append(left[i])
            i += 1

        # Append any remaining elements from the right list
        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    @staticmethod
    def merge_bsts(bst1: BinarySearchTree, bst2: BinarySearchTree) -> BinarySearchTree:
        """
            Time complexity is O(n + m) and space complexity is O(n + m).
        """

        # Merge two BSTs into a balanced BST
        bst = BinarySearchTree()

        # Get inorder traversal of both BSTs
        inorder1 = []
        Solution.get_inorder(bst1.root, inorder1)

        inorder2 = []
        Solution.get_inorder(bst2.root, inorder2)

        # Merge the two inorder lists into a single sorted list
        inorder = Solution._get_merged_inorder(inorder1, inorder2)

        # Build a balanced BST from the merged sorted list
        Solution._balanced_insert(bst, inorder, 0, len(inorder) - 1)
        return bst

    @staticmethod
    def _balanced_insert(bst, inorder, low, high):
        # Recursively insert elements to form a balanced BST from sorted inorder list
        if low > high:
            return
        mid = int(low + (high - low)/2)
        bst.insert(inorder[mid])
        Solution._balanced_insert(bst, inorder, low, mid - 1)
        Solution._balanced_insert(bst, inorder, mid + 1, high)


def construct_bst_from_array(arr):
    bst = BinarySearchTree()
    for x in arr:
        bst.insert(x)
    return bst


# Example 1
bst1 = construct_bst_from_array([100, 50, 300, 20, 70])
bst2 = construct_bst_from_array([80, 40, 120])
# This will take O(n + m) time and O(n + m) space.
bst = Solution.merge_bsts(bst1, bst2)
print("Merged BST for Example 1:")
bst.show()

# Example 2
bst3 = construct_bst_from_array([3, 1, 5])
bst4 = construct_bst_from_array([4, 2, 6])
bst34 = Solution.merge_bsts(bst3, bst4)
print("Merged BST for Example 2:")
bst34.show()

# Example 3
bst5 = construct_bst_from_array([5, 3, 0])
bst6 = construct_bst_from_array([8, 2, 1, 10])
bst56 = Solution.merge_bsts(bst5, bst6)
print("Merged BST for Example 3:")
bst56.show()
