# Problem link - https://www.geeksforgeeks.org/convert-bst-min-heap/


class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert(self, start, node):
        if node is None or start is None:
            return

        if node.data >= start.data:
            if start.right is not None:
                return self._insert(start.right, node)
            start.right = node
            return

        if start.left is not None:
            return self._insert(start.left, node)
        start.left = node
        return

    def insert(self, x):
        node = Node(x)
        if self.root is None:
            self.root = node
            return
        return self._insert(self.root, node)

    def _get_inorder(self, start, inorder):
        if start:
            self._get_inorder(start.left, inorder)
            inorder.append(start)
            self._get_inorder(start.right, inorder)

    def get_inorder(self):
        inorder = []
        self._get_inorder(self.root, inorder)
        return inorder

    def _get_preorder(self, start, preorder):
        if start:
            preorder.append(start)
            self._get_preorder(start.left, preorder)
            self._get_preorder(start.right, preorder)

    def get_preorder(self):
        preorder = []
        self._get_preorder(self.root, preorder)
        return preorder

    def _show(self, start):
        if start:
            self._show(start.left)
            print(f"Data = {start.data}{' (root)' if start == self.root else ''}")
            self._show(start.right)

    def show(self):
        self._show(self.root)


class BstToMinHeapConvertor:
    def __init__(self):
        pass

    def convert(self, binary_search_tree: BinarySearchTree):
        # Overall time complexity is O(N) and overall space complexity is O(N).

        # This takes O(N) time and O(N) space for both traversals.
        inorder = binary_search_tree.get_inorder()
        preorder = binary_search_tree.get_preorder()

        # This will take another O(N) time
        inorder = [i.data for i in inorder]

        # This will take another O(N) time.
        for i in range(len(preorder)):
            preorder[i].data = inorder[i]


tree = BinarySearchTree()
tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.show()
print()
bst_to_min_heap_convertor = BstToMinHeapConvertor()
bst_to_min_heap_convertor.convert(tree)
tree.show()